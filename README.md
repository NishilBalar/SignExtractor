# SignExtractor
A mini project work to extract sign from scanned documment using image processing techniques. This project provides basic signature exraction from high quality scanned document

  The 4 stage followed to fulfill task is:

- [Page Cropping - Transformation of perspective](https://github.com/NishilBalar/SignExtractor/blob/master/crop_edge.py)
- [Signatre extraction](https://github.com/NishilBalar/SignExtractor/blob/master/sign_extractor.py)
- [Softening mask](https://github.com/NishilBalar/SignExtractor/blob/master/soften.py)
- [Color adjustion](https://github.com/NishilBalar/SignExtractor/blob/master/color_adjust.py)

## Example of application of algorithm to extract signature

- Input = The digital photo of the document (scanned from mobile or printer) 
- Output = The signatures exist on the input

  Note: Here, I used my experience certificate as input image which is being scanned from mobile camera. Output with extracted image is shown below.

<p align="center">
  <img src="https://github.com/NishilBalar/SignExtractor/blob/master/result.gif" | width=450>
</p>

**Summary:** Firstly, the page cropping algorithm is performed to transform scanned document to page perspective. After that, Signatre extraction algorithm is being performed to extract sign from scanned documents. At last, softening and colour adjustment algorithm are performed to get output document with high quality! 


## Installation & Run

**1.) pip library installation**

- Python version requirements: 3.3+

Create virtual environment and install all required dependencies as stated in requirement.txt file as follow in command prompt

```
python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

```

**2.) Run code to extract signature**
After adding your desired image as `test.jpg`, run following command in command prompt to run signature extraction algorithm!

```
python -m magic

```

## Acknowledgement
    @ONLINE{hse,
            author = "Ahmet Özlü",
            title  = "Overlapped handwritten signature extraction from scanned documents",
            year   = "2018",
            url    = "https://github.com/ahmetozlu/signature_extractor"
        }



