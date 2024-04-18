from django.db import models


class VariationManager(models.Manager):
    def colour(self):
        return super(VariationManager, self).filter(variation_category='colour', is_active=True)

    def mapping(self):
        return super(VariationManager, self).filter(variation_category='mapping', is_active=True)

    def air_filter(self):
        return super(VariationManager, self).filter(variation_category='air filter', is_active=True)

    def silicon_hose_colour(self):
        return super(VariationManager, self).filter(variation_category='silicon hose colour', is_active=True)

    def intercooler(self):
        return super(VariationManager, self).filter(variation_category='intercooler', is_active=True)

    def catalyst(self):
        return super(VariationManager, self).filter(variation_category='catalyst', is_active=True)

    def pf_back_exhaust(self):
        return super(VariationManager, self).filter(variation_category='PF-Back Exhaust', is_active=True)

    def gpf_Delete(self):
        return super(VariationManager, self).filter(variation_category='GPF Delete', is_active=True)
