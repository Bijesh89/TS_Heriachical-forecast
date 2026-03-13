import pandas as pd

def build_hierarchy():

    bottom = [
        "Region_A_Product_1",
        "Region_A_Product_2",
        "Region_B_Product_1",
        "Region_B_Product_2"
    ]

    S = pd.DataFrame(
        [
            [1,1,1,1],   # Total
            [1,1,0,0],   # Region_A
            [0,0,1,1],   # Region_B
            [1,0,0,0],   # Region_A_Product_1
            [0,1,0,0],   # Region_A_Product_2
            [0,0,1,0],   # Region_B_Product_1
            [0,0,0,1],   # Region_B_Product_2
        ],
        columns=bottom
    )

    S.index = [
        "Total",
        "Region_A",
        "Region_B",
        "Region_A_Product_1",
        "Region_A_Product_2",
        "Region_B_Product_1",
        "Region_B_Product_2"
    ]

    tags = {
        "Total": ["Total"],
        "Region": ["Region_A","Region_B"],
        "Bottom": bottom
    }

    return S, tags