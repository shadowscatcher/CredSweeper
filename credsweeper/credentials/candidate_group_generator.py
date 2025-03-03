from typing import List, Dict, Tuple

from credsweeper.credentials.candidate import Candidate
from credsweeper.credentials.candidate_key import CandidateKey


class CandidateGroupGenerator:
    def __init__(self) -> None:
        self.grouped_candidates: Dict[CandidateKey, List[Candidate]] = {}

    @property
    def grouped_candidates(self) -> Dict[CandidateKey, List[Candidate]]:
        return self._grouped_candidates

    @grouped_candidates.setter
    def grouped_candidates(self, grouped_candidates: Dict[CandidateKey, List[Candidate]]) -> None:
        self._grouped_candidates = grouped_candidates

    def __contains__(self, key: CandidateKey) -> bool:
        return key in self.grouped_candidates

    def __getitem__(self, key) -> List[Candidate]:
        return self.grouped_candidates[key]

    def __setitem__(self, key: CandidateKey, value: List[Candidate]) -> None:
        self.grouped_candidates[key] = value

    def __len__(self) -> int:
        return len(self.grouped_candidates)

    def items(self) -> List[Tuple[CandidateKey, List[Candidate]]]:
        return list(self.grouped_candidates.items())
