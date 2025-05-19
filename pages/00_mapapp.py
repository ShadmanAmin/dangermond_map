import leafmap
import solara
import rasterio
from ipyleaflet import Popup, GeoJSON
from ipywidgets import HTML, VBox, Button, Layout, Image as WImage
from shapely.geometry import shape

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
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree1.shp', layer_name='tree1')
        self.add_shp('/home/jovyan/src/tree_shapefiles/tree3.shp', layer_name='tree3')
        self.add_shp('/home/jovyan/src/tree_shapefiles/base_station.shp', layer_name='base_station')
        # Manually find GeoJSON layers by name
        self.tree1_layer = next(
            (ly for ly in self.layers if hasattr(ly, 'name') and ly.name=='tree1' and isinstance(ly, GeoJSON)),
            None
        )
        self.tree3_layer = next(
            (ly for ly in self.layers if hasattr(ly, 'name') and ly.name=='tree3' and isinstance(ly, GeoJSON)),
            None
        )
        self.base_station_layer = next(
            (ly for ly in self.layers if hasattr(ly, 'name') and ly.name=='base_station' and isinstance(ly, GeoJSON)),
            None
        )
        # Attach click handlers
        if self.tree1_layer:
            self.tree1_layer.on_click(self.on_tree1_click)
        if self.tree3_layer:
            self.tree3_layer.on_click(self.on_tree3_click)
        if self.base_station_layer:
            self.base_station_layer.on_click(self.on_base_click)
        # Add layer control to map
        self.add_layer_control()

    def on_tree1_click(self, event, feature, **kwargs):
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y
        # Title and image
        title = HTML(value="<b>HAH THIS IS DANGERMOND!</b>")
        img_url = feature['properties'].get(
            'img_url',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Jack_Dangermond_in_2012.jpg/250px-Jack_Dangermond_in_2012.jpg'
        )
        image = HTML(value=f"""
            <div style="text-align:center">
              <img src="{img_url}" style="width:auto; height:auto; display:block; margin:auto;">
            </div>
        """)
        close_btn = Button(description='Close', button_style='danger')
        container = VBox([title, image, close_btn], layout=Layout(width='auto', height='auto', align_items='center'))
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
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)
        self.add(popup)

    def on_tree3_click(self, event, feature, **kwargs):
        geom = feature['geometry']
        if geom['type'] == 'Point':
            lon, lat = geom['coordinates']
        else:
            centroid = shape(geom).centroid
            lon, lat = centroid.x, centroid.y
        # Load local image
        with open('/home/jovyan/src/images/broken_tree.JPG', 'rb') as f:
            img_bytes = f.read()
        img_widget = WImage(value=img_bytes, format='jpg', layout=Layout(max_width='600px', max_height='400px'))
        title = HTML(value="<b>Broken Tree!</b>")
        close_btn = Button(description='Close', button_style='danger')
        container = VBox([title, img_widget, close_btn], layout=Layout(width='auto', align_items='center'))
        popup = Popup(location=(lat, lon), child=container, close_button=False, auto_close=False, close_on_click=False, close_on_escape_key=False, min_width=400, min_height=300)
        def _on_close_clicked(btn):
            self.remove_layer(popup)
        close_btn.on_click(_on_close_clicked)
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