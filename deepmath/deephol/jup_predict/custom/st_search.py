from deepmath.deephol import predictions

def _proof_state_from_search(predictor, node):
    return predictor.ProofState(goal='goal')
