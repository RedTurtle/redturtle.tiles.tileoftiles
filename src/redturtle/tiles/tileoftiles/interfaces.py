# -*- coding: utf-8 -*-
from plone.namedfile.field import NamedBlobFile
from plone.supermodel import model
from redturtle.tiles.management.interfaces import IRedturtleTilesManagementLayer
from redturtle.tiles.tileoftiles import _
from zope import schema


class IRedturtleTilesTileoftilesLayer(IRedturtleTilesManagementLayer):
    """Marker interface that defines a browser layer."""


class ITileOfTiles(model.Schema):
    """ """

    title = schema.TextLine(
        title=_("label_tile_title", u"Title title"), required=False
    )

    background_color = schema.TextLine(
        title=_("Please set a hex code"),
        description=_("This property will be overriden by background image"),
        required=False,
    )

    background_image = NamedBlobFile(
        title=_(u"Please, upload an image"), required=False
    )

    min_height = schema.TextLine(
        title=_(
            "Write here class or list of classes that will be added to the tile view"
        ),
        default=u"200px",
        required=False,
    )

    css_class = schema.TextLine(
        title=_(
            "Write here class or list of classes that will be added to the tile view"
        ),
        required=False,
    )
