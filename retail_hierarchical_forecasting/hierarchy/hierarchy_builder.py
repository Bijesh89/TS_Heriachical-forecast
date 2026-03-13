def build_tags(df):

    tags = {
        "region":df["region"].unique(),
        "store":df["store"].unique(),
        "category":df["category"].unique()
    }

    return tags