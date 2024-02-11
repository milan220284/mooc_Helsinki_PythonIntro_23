# Write your solution here:
def  sort_by_seasons(items: dict):
    def order_by_numberOfSeasons(item):
        return(item["seasons"])
    
    return sorted(items, key=order_by_numberOfSeasons)


