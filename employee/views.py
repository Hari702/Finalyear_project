from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from employee.forms import EmployeeForm

from django.views.generic import DetailView
from employee.models import Employee
from textblob import TextBlob


class EmployeeImage(TemplateView):
    form = EmployeeForm
    template_name = 'emp_image.html'

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save()

            return HttpResponseRedirect(reverse_lazy('emp_image_display', kwargs={'pk': obj.id}))

        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'


def plant(request):
    result1 = Employee.objects.latest('id')
    import numpy as np
    import tensorflow as tf
    from tensorflow import keras
    import h5py
    # models = keras.models.load_model('C:/Users/admin/Desktop/E1192-FINAL/CODE/Deploy/employee/plant1.h5')
    models = keras.models.load_model('D:/FinalYear_Project/E1192-FINAL/E1192-FINAL/CODE/plant1.h5')
    # models = keras.models.load_model('D:/Demo_finalyear_project/plant1.h5')

    from tensorflow.keras.preprocessing import image
    # test_image = image.load_img('C:/Users/admin/Desktop/E1192-FINAL/CODE/Deploy/media/' + str(result1),
    #                             target_size=(225, 225))
    test_image = image.load_img('D:/FinalYear_Project/E1192-FINAL/E1192-FINAL/CODE/Deploy/media/' + str(result1),
                                                           target_size=(225, 225))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = models.predict(test_image)
    prediction = result[0]
    prediction = list(prediction)
    classes=['Apple Disease','Apple healthy','Cherry Disease','Cherry healthy','Grape Disease','Grape healthy','Peach Bacterial','Peach healthy','Strawberry Disease','Strawberry healthy']
    output = zip(classes, prediction)
    output = dict(output)
    if output['Apple Disease'] == 1.0:
        a = "Apple Disease Leaf"
        # b='emp_image_Tam.html'
        b="You can spot powdery mildew by its fluffy white presence on leaves and branches. To treat powdery mildew, spray your apple trees with lime sulfur and prune away any mildew-infested shoots. Prevent the mildew from returning in the spring by cleaning up leaves in the fall."
    elif output['Apple healthy'] == 1.0:
        a = "Apple healthy Leaf"
        b=""
    elif output['Cherry Disease'] == 1.0:
        a = "Cherry Disease Leaf"
        b="""Symptoms: This disease infects the leaves of cherry trees, which may appear on leaf petioles and fruit pedicels. 
             Several small size purple spots develop on the upper side of the leaf. All these spots will enlarge to around 
             1/4-inch in diameter,which converts into a reddish-brown color. These spots will fall down once they are dry, 
             which takes around 6-8 weeks.It ends up creating small holes in the leaf, while at times, the older infected 
             leaves may become golden yellow before falling off.The cherry leaves are infected with cherry leaf spots that 
             may fall prematurely. 
        
             Causes: This disease is mainly seen during the early spring making the leaves dead. During the early days of springs,
             we see the fruiting bodies develop mainly on the leaves, producing spores. The rainfall spreads all these spores to 
             healthy leaves, where spores are seen germinating and penetrating the leaf. These are mostly seen over the leaf once
             it infects them, while the spots are developed with the undersides that are seen growing the fungal spores that appear
             like whitish pink underleaf lesions. 
          
             Treatment: All you need to do is to collect all the fallen leaves and destroy them to prevent the fungus from overwintering.
             It can help remove the leaves for an effective solution for backyard cherry that can help grow the trees. But it can help 
             add up the limitations for many more big-time cherry orchards. It helps plant the cherry tree to give direct sunlight and
             allow good air circulation. Using fungicides is an effective method to fix this problem for big-size lawns or commercial 
             orchards."""

    elif output['Cherry healthy'] == 1.0:
        a = "Cherry healthy Leaf"
        b=""
    elif output['Grape Disease'] == 1.0:
        a = "Grape Disease Leaf"
        b="Spraying of the grapevines at 3-4 leaf stage with fungicides like Bordeaux mixture @ 0.8% or Copper Oxychloride @ 0.25% or Carbendazim @ 0.1% are effective against this disease."
    elif output['Grape healthy'] == 1.0:
        a = "Grape healthy Leaf"
        b=""

    elif output['Peach Bacterial'] == 1.0:
        a = "Peach Bacterial Leaf"
        b="To control Peach Leaf Curl, treat Peach and Nectarine trees with a fungicide in the fall after leaves have dropped. In the past, the disease could be successfully treated with either lime-sulfur fungicide or a fixed copper fungicide with a copper compound containing at least 50 percent copper."
    elif output['Peach healthy'] == 1.0:
        a = "Peach healthy Leaf"
        b=""
    elif output['Strawberry Disease'] == 1.0:
        a = "Strawberry Disease Leaf"
        b="To control Peach Leaf Curl, treat Peach and Nectarine trees with a fungicide in the fall after leaves have dropped. In the past, the disease could be successfully treated with either lime-sulfur fungicide or a fixed copper fungicide with a copper compound containing at least 50 percent copper."
#         c="""Some general tips that may help to prevent or treat strawberry leaf diseases include:
# 1.Keep the strawberry plants healthy by providing proper nutrition, watering, and pruning.
# 2.Remove and destroy infected leaves and plant debris.
# 3.Apply fungicides or other treatments as recommended by a professional or the manufacturer.
# 4.Use cultural practices, such as mulching and proper plant spacing, to increase air circulation and reduce humidity around the strawberry plants."""
    elif output['Strawberry healthy'] == 1.0:
        a = "Strawberry healthy Leaf"
        b=""


    # return render(request, "result.html", {"out": a})
    return render(request,"result.html", {"out": a,"in":b})
