from Parents import ButtonBrowse
from config_data import current_config


class MapsetButton(ButtonBrowse):
	def __init__(self, parent):
		super(MapsetButton, self).__init__(parent)

		self.default_x = 505
		self.default_y = 85
		self.default_size = 3.35
		self.file_type = "Folder"

		self.img_idle = "res/B2_Idle.png"
		self.img_hover = "res/B2_Hover.png"
		self.img_click = "res/B2_Click.png"
		self.img_shadow = "res/B2_Shadow.png"

		super().setup()

	def afteropenfile(self, filename):
		if filename == "":  # if user cancel select
			return
		current_config["Beatmap path"] = filename
		self.main_window.mapsetpath.setText(filename)
