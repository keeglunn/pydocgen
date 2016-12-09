from docx import Document
import itertools

lorem_ipsum = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nulla ipsum, rhoncus malesuada sapien vel, lacinia scelerisque diam. Aenean ut lorem dui. Curabitur sit amet feugiat libero. Sed eu rhoncus ligula, vitae tristique neque. Ut felis est, gravida at ipsum sit amet, auctor ultricies purus. Aliquam nec mauris quis ligula viverra condimentum nec in augue. Integer non bibendum metus. Donec feugiat risus ut neque scelerisque finibus. Suspendisse consectetur erat a efficitur viverra.",
"Nulla vehicula dictum lorem vel tristique. Donec scelerisque, ipsum ut rutrum tristique, lacus magna consectetur nibh, et tincidunt nisl velit eu enim. Aliquam elementum erat eget sapien ullamcorper consectetur. Nullam efficitur leo pharetra nunc tristique, sit amet commodo sem gravida. Pellentesque eleifend diam vitae viverra tincidunt. Quisque interdum lacus dui, non feugiat lectus fringilla at. Suspendisse sollicitudin tellus et purus convallis porta. Morbi laoreet neque vel risus sollicitudin, ut semper magna tempor. Nunc erat nisi, maximus et felis vitae, rhoncus sollicitudin diam.",
"Sed turpis elit, tincidunt non luctus non, rhoncus et tortor. Aenean felis erat, ultricies sit amet tincidunt et, efficitur quis justo. Duis a eleifend nibh, a ullamcorper ex. Aenean vehicula velit tortor, quis faucibus quam tristique eu. Nulla facilisi. Duis sollicitudin eleifend tincidunt. Curabitur a sodales mi. Sed molestie cursus mollis. Proin porta leo ut massa volutpat, et hendrerit ipsum tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce convallis orci quis magna iaculis mattis. Maecenas egestas velit ipsum, eget scelerisque arcu egestas malesuada.",
"Suspendisse sed tincidunt tellus. Aliquam eget lorem blandit, tempus libero ut, posuere mauris. Morbi sollicitudin diam id ultrices efficitur. Aenean nec est eget sapien dignissim faucibus. Nulla facilisi. Praesent enim lectus, finibus nec odio vel, condimentum condimentum neque. Curabitur sapien diam, mattis et imperdiet pharetra, facilisis non nisi. Praesent porttitor lorem sed arcu porta, nec hendrerit odio mollis. Nam eu blandit ligula. Curabitur justo elit, ultrices sit amet lacinia sit amet, tristique ut purus. Nulla facilisi. In facilisis sit amet lorem at varius. Nam dui dui, sollicitudin a consectetur quis, suscipit nec quam. Cras leo ante, lacinia quis aliquam at, ultricies semper eros.",
"Phasellus rhoncus sem vitae nulla rhoncus vulputate. Maecenas tempor dapibus magna, sit amet blandit dolor aliquam a. Integer ut pulvinar massa, in tincidunt diam. Morbi id iaculis enim. Duis at dolor eu augue placerat sodales. Donec at congue urna. Nam et turpis maximus, placerat nisl dapibus, maximus tellus. Mauris aliquet tortor in felis mollis egestas. Duis et nisl vitae eros consequat semper. Maecenas quis nibh fringilla, ullamcorper sapien ut, feugiat sapien."]

lorem_ipsum_bytes = 3124

def generate_docx(size_in_kb, path):
    document = Document()

    scale = int((size_in_kb * 1000) / lorem_ipsum_bytes)
    
    for x in itertools.chain([lorem_ipsum for x in range(scale)]):
        document.add_paragraph(x)
    document.save(path)

def makeSquareImg(width):
    import Image, ImageDraw

    size = (width, width)
    image = Image.new('RGB', size)

    