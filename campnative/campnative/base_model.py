from model_utils.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    def __unicode__(self):
        return self.__string__()

    def __repr__(self):
        return self.__string__()

    class Meta:
        abstract = True
