from hierarchicalforecast.methods import BottomUp, MinTrace
from hierarchicalforecast.core import HierarchicalReconciliation

def reconcile(Y_hat_df,S,tags):

    reconcilers = [
        BottomUp(),
        MinTrace(method="ols")
    ]

    hrec = HierarchicalReconciliation(
        reconcilers=reconcilers
    )

    Y_rec_df = hrec.reconcile(
        Y_hat_df=Y_hat_df,
        S=S,
        tags=tags
    )

    return Y_rec_df