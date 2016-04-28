from json import dumps
from lxml import objectify


class Conversion(object):
    """
    Class Converting and XML File's Contents into a JSON Object
    """
    def __init__(self, xml):
        """
        Initialize Variables and Receive XML String
        :param xml:
        :return:
        """
        self.xml = xml

    def xml_to_json(self):
        """
        Begin the XML String by Determining Format of XML
        Objectify the XML and send to Convert to JSON via Function _to_json
        :return: The XML String
        """
        xml_object = self.xml if isinstance(self.xml, objectify.ObjectifiedElement) \
            else objectify.fromstring(self.xml)

        return dumps({xml_object.tag: Conversion._to_json(xml_object)})

    @staticmethod
    def _to_json(xml_object):
        """
        Receives XML Parsings from xml_to_json function
        Parses through XML and Determines Elements, Attributes, and Lists within the XML

        :return: Dictionary formatted Items
        """
        attributes = None
        if hasattr(xml_object, "attrib") and not xml_object.attrib == {}:
            attributes = xml_object.attrib

        if isinstance(xml_object, objectify.ObjectifiedElement):
            return Conversion._element_to_json(xml_object, attributes)

        if isinstance(xml_object, list):
            if len(xml_object) > 1 and all(xml_object[0].tag == item.tag for item in xml_object):
                return [Conversion._to_json(attr) for attr in xml_object]

            return dict([(item.tag, Conversion._to_json(item)) for item in xml_object])

        return Exception("Not a Valid XML Object")

    @staticmethod
    def _element_to_json(xml_element, attributes):
        """
        Converts Individual Elements to JSON Format
        Flattens Attributes
        :return: Converted Elements, Attributes, and Values
        """
        if isinstance(xml_element, objectify.BoolElement):
            return Conversion._flatten_attr(xml_element.tag, bool(xml_element), attributes)

        if isinstance(xml_element, objectify.IntElement):
            return Conversion._flatten_attr(xml_element.tag, int(xml_element), attributes)

        if isinstance(xml_element, objectify.FloatElement):
            return Conversion._flatten_attr(xml_element.tag, float(xml_element), attributes)

        if isinstance(xml_element, objectify.StringElement):
            return Conversion._flatten_attr(xml_element.tag, str(xml_element).strip(), attributes)

        return Conversion._flatten_attr(xml_element.tag, Conversion._to_json(xml_element.getchildren()), attributes)

    @staticmethod
    def _flatten_attr(property_name, lookup, attributes):
        """
        Adds Attributes of and XML Namespace to the JSON Dictionary
        This is used so as not to discard potentially useful information
        :return: Flattened Attributes
        """
        if attributes is None:
            return lookup

        if not isinstance(lookup, dict):
            return dict(attributes.items() + [(property_name, lookup)])

        return dict(lookup.items() + attributes.items())
