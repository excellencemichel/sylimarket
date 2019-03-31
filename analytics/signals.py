from django.dispatch import Signal

object_viewed_signal = Signal(providing_args = ["intance", "request"])


product_purshase_create_signal = Signal(providing_args = ["product_id"])
