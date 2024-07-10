from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .ai_models import DataExtractor
from .document_processor import DocumentProcessor  # Import the DocumentProcessor

@csrf_exempt
def upload_form(request):
    return render(request, 'upload_form.html')

@csrf_exempt
def extract_data(request):
    if request.method == 'POST':
        model_name = request.POST.get('model_name')
        uploaded_file = request.FILES.get('file')
        
        if not model_name or not uploaded_file:
            return JsonResponse({"error": "Both model_name and file are required"}, status=400)
        
        credentials = {}  # Add any necessary credentials
        
        try:
            # Read the content of the uploaded file
            try:
                file_content = uploaded_file.read()
                
                # Determine file type and process accordingly using DocumentProcessor
                if uploaded_file.name.endswith('.pdf'):
                    result = DocumentProcessor.read_pdf(file_content)
                elif uploaded_file.name.endswith('.docx'):
                    result = DocumentProcessor.read_docx(file_content)
                elif uploaded_file.name.endswith('.csv'):
                    result = DocumentProcessor.read_csv(file_content)
                else:
                    # Handle unsupported file types or binary data
                    result = file_content
                
                # Process further with the AI model if needed
                extractor = DataExtractor(model_name, credentials)
                result = extractor.extract_data(result, "extract_text", "json")
                
                return JsonResponse({"result": result})
            
            except Exception as e:
                # Log the exception for debugging purposes
                print("Exception occurred:", str(e))
                return JsonResponse({"error": str(e)}, status=400)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)



from django.shortcuts import render

def upload_form(request):
    return render(request, 'upload_form.html')