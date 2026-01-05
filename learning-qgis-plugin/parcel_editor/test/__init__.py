# import qgis libs so that ve set the correct sip api version
import qgis   # pylint: disable=W0611  # NOQA


def classFactory(iface):
    from .test import Test
    return Test(iface)