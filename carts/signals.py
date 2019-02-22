from django.dispatch import Signal

cart_item_added_signal = Signal(providing_args = ["action"])