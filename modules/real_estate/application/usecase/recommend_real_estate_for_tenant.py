from __future__ import annotations

from modules.real_estate.application.dto.recommendation_dto import (
    RecommendListingsQuery,
    RecommendResult,
    RecommendedListing,
)
from modules.real_estate.application.port_out.real_estate_embedding_search_port import (
    RealEstateEmbeddingSearchPort,
)
from modules.real_estate.application.port_out.tenant_request_embedding_port import (
    TenantRequestEmbeddingReadPort,
)


class RecommendRealEstateForTenantService:
    """tenant_request 임베딩 기반 매물 추천."""

    def __init__(
        self,
        tenant_embedding_reader: TenantRequestEmbeddingReadPort,
        real_estate_search: RealEstateEmbeddingSearchPort,
    ):
        self.tenant_embedding_reader = tenant_embedding_reader
        self.real_estate_search = real_estate_search

    async def execute(self, query: RecommendListingsQuery) -> RecommendResult:
        vec = self.tenant_embedding_reader.get_vector(query.tenant_request_id)
        if vec is None:
            return RecommendResult(listings=[])
        search_results = self.real_estate_search.search_similar(
            vec, top_n=query.top_n
        )
        listings = [
            RecommendedListing(real_estate_list_id=item_id, score=score)
            for item_id, score in search_results
        ]
        return RecommendResult(listings=listings)
