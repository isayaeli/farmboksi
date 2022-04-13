from django.contrib import admin
from .models import Auction, Bider,BidDate
# Register your models here.
admin.site.register(Auction)
admin.site.register(Bider)
admin.site.register(BidDate)