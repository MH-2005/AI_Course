from django import forms


class ImageEditForm(forms.Form):
    image = forms.ImageField(
        label="Upload an image",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

    apply_contrast = forms.BooleanField(required=False, label="Adjust Contrast/Brightness")
    apply_drawing = forms.BooleanField(required=False, label="Draw on Image")

    contrast = forms.FloatField(
        label="Contrast",
        min_value=0.1, max_value=3.0,
        initial=1.0, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-range', 'type': 'range', 'step': '0.1'})
    )
    brightness = forms.IntegerField(
        label="Brightness",
        min_value=-100, max_value=100,
        initial=0, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-range', 'type': 'range', 'step': '1'})
    )

    DRAW_CHOICES = [('line', 'Line'), ('rectangle', 'Rectangle')]
    draw_type = forms.ChoiceField(
        choices=DRAW_CHOICES,
        widget=forms.RadioSelect,
        initial='line',
        required=False
    )

    draw_color = forms.CharField(
        label="Color (R,G,B)",
        initial="255,0,0", max_length=11, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    draw_thickness = forms.IntegerField(
        label="Thickness",
        min_value=1, max_value=50,
        initial=2, required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'})
    )

    line_x1 = forms.IntegerField(label="Start X1", min_value=0, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    line_y1 = forms.IntegerField(label="Start Y1", min_value=0, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    line_x2 = forms.IntegerField(label="End X2", min_value=0, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    line_y2 = forms.IntegerField(label="End Y2", min_value=0, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))

    rect_x1 = forms.IntegerField(label="Top-Left X1", min_value=0, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    rect_y1 = forms.IntegerField(label="Top-Left Y1", min_value=0, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    rect_x2 = forms.IntegerField(label="Bottom-Right X2", min_value=0, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    rect_y2 = forms.IntegerField(label="Bottom-Right Y2", min_value=0, required=False,
                                 widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))

    def clean_draw_color(self):
        color_str = self.cleaned_data.get('draw_color')

        if not color_str:
            return None

        try:
            r, g, b = map(int, color_str.split(','))
            return (b, g, r)
        except (ValueError, TypeError):
            raise forms.ValidationError("Invalid color format. Use R,G,B (e.g., '255,0,0').")
