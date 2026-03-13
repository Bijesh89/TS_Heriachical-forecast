from hierarchicalforecast.methods import BottomUp
from hierarchicalforecast.core import HierarchicalReconciliation

def reconcile_forecasts(forecasts, S, tags):

    reconcilers = [BottomUp()]

    hrec = HierarchicalReconciliation(reconcilers=reconcilers)

    Y_rec_df = hrec.reconcile(
        Y_hat_df=forecasts,
        S=S,
        tags=tags
    )

    return Y_rec_df