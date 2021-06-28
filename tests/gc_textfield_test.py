import unittest
from googleforms.bot_forms import BotForms


class TextFieldTest(unittest.TestCase):
    website_url = "https://forms.gle/rUd5fBs5CPJv5ML29"
    name_title_field = "Resposta curta"
    insert_text = "texto aleatorio a ser inserido"
    path_base_root = "freebirdFormviewerComponentsQuestionBaseRoot"
    bf = None

    def setUp(self):
        self.bf = BotForms()
        self.bf._BotForms__start_driver()
        self.bf._BotForms__open_page(self.website_url)

    def tearDown(self):
        self.bf._BotForms__stop_driver()

    def test_get_element_by_title(self):
        # Testa se pegou o elemento pelo titulo.
        title_component = self.bf._BotForms__text_field_get_by_title(
            self.name_title_field)

        self.assertIn(self.name_title_field, title_component.text)

    def test_get_root_ancestral(self):
        # Testa se pegou o pai principal do componente.
        title_component = self.bf._BotForms__text_field_get_by_title(
            self.name_title_field)

        root_ancestor = self.bf._BotForms__text_field_get_root_ancestral(
            title_component)

        self.assertIn(self.path_base_root,
                      root_ancestor.get_attribute("class"))

    def test_filled_field(self):
        # Testa se inseriu corretamente o texto no campo.
        self.bf._BotForms__text_field(
            self.name_title_field, self.insert_text)

        title_component = self.bf._BotForms__text_field_get_by_title(
            self.name_title_field)
        root_ancestor = self.bf._BotForms__text_field_get_root_ancestral(
            title_component)
        input_field = root_ancestor.find_element_by_tag_name("input")

        self.assertIn(self.insert_text, input_field.get_attribute("value"))


if __name__ == "__main__":
    unittest.main()
