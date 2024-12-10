from django.contrib import admin

import application.models.accounts as account_models
import application.models.bnb as bnb_models

# Register your models here.
admin.site.register(account_models.Account)
admin.site.register(account_models.Owner)
admin.site.register(account_models.WishList)
admin.site.register(account_models.WishListItems)
admin.site.register(account_models.Booking)

admin.site.register(bnb_models.BnbInformation)
admin.site.register(bnb_models.Category)
admin.site.register(bnb_models.Image)
admin.site.register(bnb_models.Location)
admin.site.register(bnb_models.Rule)
admin.site.register(bnb_models.Review)
admin.site.register(bnb_models.Service)
