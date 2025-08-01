import os
import uuid

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from .forms import ImageEditForm
from .image_processor import ImageProcessor


def _clear_session_files(request):
    fs = FileSystemStorage()
    original_path = request.session.get('original_image_path')
    edited_path = request.session.get('edited_image_path')

    if edited_path and edited_path != original_path and fs.exists(edited_path.split('/')[-1]):
        fs.delete(edited_path.split('/')[-1])

    if original_path and fs.exists(original_path.split('/')[-1]):
        fs.delete(original_path.split('/')[-1])


def edit_image_view(request):
    form = ImageEditForm(request.POST or None, request.FILES or None)
    context = {'form': form}

    if 'original_image_path' in request.session:
        context['original_image_url'] = request.session.get('original_image_path')
        context['edited_image_url'] = request.session.get('edited_image_path')

    if request.method == 'POST' and form.is_valid():
        fs = FileSystemStorage()
        uploaded_file = form.cleaned_data.get('image')

        if uploaded_file:
            _clear_session_files(request)

            ext = uploaded_file.name.split('.')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            saved_path = fs.save(filename, uploaded_file)

            request.session['original_image_path'] = fs.url(saved_path)
            request.session['edited_image_path'] = fs.url(saved_path)

            return redirect('edit_image')

        elif 'original_image_path' in request.session:
            original_filename = request.session['original_image_path'].split('/')[-1]
            full_original_path = os.path.join(settings.MEDIA_ROOT, original_filename)

            processor = ImageProcessor(full_original_path)
            data = form.cleaned_data

            if data.get('apply_contrast'):
                processor.adjust_contrast_brightness(alpha=data.get('contrast'), beta=data.get('brightness'))

            if data.get('apply_drawing'):
                color = data.get('draw_color')
                thickness = data.get('draw_thickness')
                draw_type = data.get('draw_type')

                if draw_type == 'line':
                    p1 = (data.get('line_x1'), data.get('line_y1'))
                    p2 = (data.get('line_x2'), data.get('line_y2'))
                    processor.draw_line(p1, p2, color, thickness)
                elif draw_type == 'rectangle':
                    p1 = (data.get('rect_x1'), data.get('rect_y1'))
                    p2 = (data.get('rect_x2'), data.get('rect_y2'))
                    processor.draw_rectangle(p1, p2, color, thickness)

            ext = original_filename.split('.')[-1]
            edited_filename = f"edited_{uuid.uuid4()}.{ext}"
            edited_path = os.path.join(settings.MEDIA_ROOT, edited_filename)
            processor.save_image(edited_path)

            old_edited_path = request.session.get('edited_image_path')
            if old_edited_path != request.session.get('original_image_path') and fs.exists(
                    old_edited_path.split('/')[-1]):
                fs.delete(old_edited_path.split('/')[-1])

            request.session['edited_image_path'] = fs.url(edited_filename)

            return redirect('edit_image')

    return render(request, 'editor/index.html', context)


def reset_view(request):
    _clear_session_files(request)
    request.session.flush()
    return redirect('edit_image')
