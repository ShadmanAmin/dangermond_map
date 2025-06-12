import leafmap
import solara
import rasterio
from ipyleaflet import Popup, GeoJSON
from ipywidgets import HTML, VBox, Button, HBox, Layout, Image as WImage
from shapely.geometry import shape
from IPython.display import display

zoom = solara.reactive(6)
center = solara.reactive([34.5, -120.47])
class CustomMap(leafmap.Map):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Basemap
        self.add_basemap('HYBRID')
        # Raster layers
        # self.add_raster(
        #     source='/home/jovyan/src/ArmyCamp_BGBA.tif',
        #     layer_name='ArmyCamp_DiffLayer',
        #     indexes=[1,2,3]
        # )
        # self.add_raster(
        #     source='/home/jovyan/src/ArmyCamp_RGBA.tif',
        #     layer_name='ArmyCamp',
        #     indexes=[1,2,3]
        # )
        self.add_cog_layer(
            url = 'https://huggingface.co/datasets/ShadmanAmin/armycamp-geotiffs/resolve/main/ArmyCamp_BGBA_cog.tif',
            bands = [1,2,3],
            name='ArmyCamp_BGBA',
            use_client = True
        )
        self.add_cog_layer(
            url = 'https://huggingface.co/datasets/ShadmanAmin/armycamp-geotiffs/resolve/main/ArmyCamp_RGBA_cog.tif',
            bands = [1,2,3],
            name='ArmyCamp_RGBA',
            use_client = True
        )
        # Shapefile layers
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree1.shp', layer_name='tree1', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree2.shp', layer_name='tree2', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree3.shp', layer_name='tree3', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree4.shp', layer_name='tree4', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree5.shp', layer_name='tree5', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree6.shp', layer_name='tree6', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree7.shp', layer_name='tree7', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree8.shp', layer_name='tree8', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree9.shp', layer_name='tree9', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree10.shp', layer_name='tree10', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree11.shp', layer_name='tree11', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree12.shp', layer_name='tree12', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree13.shp', layer_name='tree13', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree14.shp', layer_name='tree14', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree15.shp', layer_name='tree15', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree16.shp', layer_name='tree16', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree17.shp', layer_name='tree17', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree18.shp', layer_name='tree18', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree19.shp', layer_name='tree19', info_mode=None)
        self.add_shp('/home/jovyan/src/tree_shapefiles/base_station.shp', layer_name='base_station')
        # Manually find GeoJSON layers by name
        layer_names = ['tree1', 'tree2', 'tree3', 'tree4', 'tree5', 'tree6', 'tree7', 'tree8', 'tree9', 'tree10', 'tree11', 'tree12', 'tree13', 'tree14', 'tree15', 'tree16', 'tree17', 'tree18']
        layer = next(
            (
            ly for ly in self.layers
            if getattr(ly, 'name', None) == name
            and isinstance(ly, GeoJSON)
            ),
            None
        )
        setattr(self, f"{name}_layer", layer)
        
        self.base_station_layer = next(
            (ly for ly in self.layers if hasattr(ly, 'name') and ly.name=='base_station' and isinstance(ly, GeoJSON)),
            None
        )
        # Attach click handlers
        if self.tree1_layer:
            self.tree1_layer.on_click(self.on_tree1_click)
        if self.tree2_layer:
            self.tree2_layer.on_click(self.on_tree2_click)
        if self.tree3_layer:
            self.tree3_layer.on_click(self.on_tree3_click)
        if self.tree4_layer:
            self.tree4_layer.on_click(self.on_tree4_click)
        if self.tree5_layer:
            self.tree5_layer.on_click(self.on_tree5_click)
        if self.tree6_layer:
            self.tree6_layer.on_click(self.on_tree6_click)
        if self.tree7_layer:
            self.tree7_layer.on_click(self.on_tree7_click)
        if self.tree8_layer:
            self.tree8_layer.on_click(self.on_tree8_click)
        if self.tree9_layer:
            self.tree9_layer.on_click(self.on_tree9_click)
        if self.tree10_layer:
            self.tree10_layer.on_click(self.on_tree10_click)
        if self.tree11_layer:
            self.tree11_layer.on_click(self.on_tree11_click)
        if self.tree12_layer:
            self.tree12_layer.on_click(self.on_tree12_click)
        if self.tree13_layer:
            self.tree13_layer.on_click(self.on_tree13_click)
        if self.tree14_layer:
            self.tree14_layer.on_click(self.on_tree14_click)
        if self.tree15_layer:
            self.tree15_layer.on_click(self.on_tree15_click)
        if self.tree16_layer:
            self.tree16_layer.on_click(self.on_tree16_click)
        if self.tree17_layer:
            self.tree17_layer.on_click(self.on_tree17_click)
        if self.tree18_layer:
            self.tree18_layer.on_click(self.on_tree18_click)
        if self.base_station_layer:
            self.base_station_layer.on_click(self.on_base_click)
        # Add layer control to map
        self.add_layer_control()


    def on_tree1_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/009.png'
        )

        # title
        title = HTML(value="<b>Tree 009</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="width:auto; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree2_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://drive.google.com/uc?export=view&id=YOUR_SAP_FLUX_PLOT_FILE_ID'
        )

        # title
        title = HTML(value="<b>Tree XXX</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)

    def on_tree3_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://drive.google.com/uc?export=view&id=YOUR_SAP_FLUX_PLOT_FILE_ID'
        )

        # title
        title = HTML(value="<b>Tree 052</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree4_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/013.png'
        )

        # title
        title = HTML(value="<b>Broken Tree!</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="width:auto; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree5_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/090.png'
        )

        # title
        title = HTML(value="<b>Tree 090</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree6_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/093.png'
        )

        # title
        title = HTML(value="<b>Tree 093</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree7_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/128.png'
        )

        # title
        title = HTML(value="<b>Tree 128</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree8_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/087.png'
        )

        # title
        title = HTML(value="<b>Tree 087</b>")

        # image widget 
        image = HTML()
        image.value = f"""
           <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree9_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/088.png'
        )

        # title
        title = HTML(value="<b>Tree 088</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree10_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/100.png'
        )

        # title
        title = HTML(value="<b>Tree 100</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree11_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/098.png'
        )

        # title
        title = HTML(value="<b>Tree 098</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree12_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/145.png'
        )

        # title
        title = HTML(value="<b>Tree 145</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree13_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/109.png'
        )

        # title
        title = HTML(value="<b>Tree 109</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree14_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/116.png'
        )

        # title
        title = HTML(value="<b>Tree 116</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree15_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/112.png'
        )

        # title
        title = HTML(value="<b>Tree 112</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree16_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/141.png'
        )

        # title
        title = HTML(value="<b>Tree 141</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree17_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/105.png'
        )

        # title
        title = HTML(value="<b>Tree 105</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_tree18_click(self, event, feature, **kwargs):

        # extract coordinates
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y

        # get both image URLs from properties
        img1_url = feature['properties'].get(
            'img_url',
            'https://drive.google.com/uc?export=view&id=YOUR_TREE_PHOTO_FILE_ID'
        )
        img2_url = feature['properties'].get(
            'plot_url',
            'https://github.com/ShadmanAmin/dangermond_map/raw/emma/sapflow_images/110.png'
        )

        # title
        title = HTML(value="<b>Tree 110</b>")

        # image widget 
        image = HTML()
        image.value = f"""
            <div style="text-align:center">
            <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
            </div>
        """

        # swap button
        toggle_btn = Button(description='→ View Plot', button_style='info')
        showing_plot = {'value': False}

        def _on_toggle_clicked(btn):
            if showing_plot['value']:
                # switch back to photo
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img1_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '→ View Plot'
            else:
                # switch to sap flux plot
                image.value = f"""
                    <div style="text-align:center">
                    <img src="{img2_url}" style="max-width:100%; height:auto; display:block; margin:auto;" id="tree-img">
                    </div>
                """
                toggle_btn.description = '← View Photo'
            showing_plot['value'] = not showing_plot['value']

        toggle_btn.on_click(_on_toggle_clicked)

        # close button
        close_btn = Button(description='Close', button_style='danger')
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)

        # assemble popup content
        container = VBox(
            [title, image, HBox([toggle_btn, close_btn])],
            layout=Layout(width='auto', height='auto', align_items='center')
        )

        popup = Popup(
            location=(lat, lon),
            child=container,
            close_button=False,
            auto_close=False,
            close_on_escape_key=False,
            max_width=1500,
            max_height=1300,
            min_width=500,
            min_height=500,
        )
        self.add(popup)
    def on_base_click(self, event, feature, **kwargs):
            geom = feature['geometry']
            if geom['type'] == 'Point':
                lon, lat = geom['coordinates']
            else:
                centroid = shape(geom).centroid
                lon, lat = centroid.x, centroid.y
            with open('/home/jovyan/src/images/solar.JPG', 'rb') as f:
                img_bytes = f.read()
            img_widget = WImage(value=img_bytes, format='jpg', layout=Layout(max_width='600px', max_height='400px'))
            title = HTML(value="<b>Power Station</b>")
            close_btn = Button(description='Close', button_style='danger')
            container = VBox([title, img_widget, close_btn], layout=Layout(width='auto', align_items='center'))
            popup = Popup(location=(lat, lon), child=container, close_button=False, auto_close=False, close_on_click=False, close_on_escape_key=False, min_width=400, min_height=300)
            def _on_close_clicked(btn):
                self.remove_layer(popup)
            close_btn.on_click(_on_close_clicked)
            self.add(popup)

# Solara Page element
@solara.component
def Page():
    with solara.Column(style={"min-width": "500px"}):
        CustomMap.element(
            # center=[34.5, -120.47],
            zoom=zoom.value,
            on_zoom=zoom.set,
            center = center.value,
            on_center=center.set,
            scroll_wheel_zoom=True,
            add_google_maps=True,
            height="750px",
            zoom_ctrl=True,
            measure_ctrl=True
        )
        solara.Text(f"Zoom: {zoom.value}")
        solara.Text(f"Center: {center.value}")