def sorted_cut(model, order_by, offset, limit):
    """
    model.objects.all().order_by(f"-{order_by}")[offset:limit]
    """
    cuted = model.objects.all().order_by(f"-{order_by}")[offset:limit]
    return cuted


def sort_by_total_rating(queryset):
    """
    modelhave to have a total rating.
    Recommand : sort_by_total_rating(sorted_cut(model, order_by, offset, limit))
    return => [(rating,object), , ,]
    """
    set_data = []
    for query in queryset:
        set_data.append((query.total_rating(), query))
    sorted_list = sorted(set_data, key=lambda x: x[0] if type(x[0]) == int else 0)
    return sorted_list


def sorted_by_total_rating_form_review(onlyOneModel, total):
    """
    rerutn (<Top review objects>,<Bottom review objects>)
    """
    top = onlyOneModel.review_set.all().order_by("-rating")[:total]
    bottom = onlyOneModel.review_set.all().order_by("rating")[:total]
    return (top, bottom)
