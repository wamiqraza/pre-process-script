import os
import xmltodict

def convert_coco_to_yolo(coco_xml_dir, yolo_txt_dir, class_mapping):
    for filename in os.listdir(coco_xml_dir):
        if filename.endswith(".xml"):
            with open(os.path.join(coco_xml_dir, filename), 'r') as file:
                data = xmltodict.parse(file.read())

            img_width = int(data['annotation']['size']['width'])
            img_height = int(data['annotation']['size']['height'])

            yolo_txt_path = os.path.join(yolo_txt_dir, filename.replace(".xml", ".txt"))

            with open(yolo_txt_path, 'w') as file:
                for obj in data['annotation']['object']:
                    class_name = obj['name']
                    class_id = class_mapping.get(class_name)
                    
                    if class_id is not None:
                        x_min = int(obj['bndbox']['xmin'])
                        y_min = int(obj['bndbox']['ymin'])
                        x_max = int(obj['bndbox']['xmax'])
                        y_max = int(obj['bndbox']['ymax'])

                        x_center = (x_min + x_max) / 2 / img_width
                        y_center = (y_min + y_max) / 2 / img_height
                        width = (x_max - x_min) / img_width
                        height = (y_max - y_min) / img_height

                        file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")

# Example usage
class_mapping = {
    'Freight': 0,
    # Add more class mappings as needed
}

coco_xml_dir = 'path/to/your/coco/xml/directory'
yolo_txt_dir = 'path/to/save/yolo/txt/directory'

convert_coco_to_yolo(coco_xml_dir, yolo_txt_dir, class_mapping)
