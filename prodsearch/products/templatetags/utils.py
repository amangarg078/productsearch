from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def request_parameters(context, request):
    request_params = request.GET.dict().copy()
    request_params.pop("page", None)
    if not request_params:
        return ""
    return "&" + "&".join([key + "=" + value for (key, value) in request_params.items()])


@register.filter()
def discount_price(price, discount, *args, **kwargs):
    # you would need to do any localization of the result here
    return "{:.2f}".format((price * discount) / 100)
