from django.shortcuts import render

def home(request):
    context = {
        'name': 'Pavel Rahman',
        'title': 'Junior Officer (Customer Service) | Graphic Designer',
        'company': 'bKash Limited',
        'location': 'Dhaka, Bangladesh',
        'about': 'I am a passionate and detail-oriented creative professional with a strong background in graphic design, data analysis, and customer-focused solutions. With over 5 years of professional experience across different industries, I bring a unique blend of creativity, analytical thinking, and problem-solving.',
        'skills': ['Graphic Design', 'Photo Manipulation', 'Photoshop', 'T-Shirt Design', 'Banner Design', 'UI Design', 'Data Analysis', 'Customer Service'],
        'projects': [
            {
                'name': 'Aviation Login Page',
                'description': 'A clean and modern aviation-themed login page design.',
                'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/fc97e8232901169.Y3JvcCwxOTUyLDE1MjcsNzcsMA.jpg',
                'link': 'https://www.behance.net/gallery/232901169/Aviation-Login-Page'
            },
            {
                'name': 'Food Banner Advertisement',
                'description': 'Eye-catching food banner for advertisement purposes.',
                'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/41fa69218801579.67a761984fb2c.jpg',
                'link': 'https://www.behance.net/gallery/218801579/Food-Banner-Advertisement'
            },
            {
                'name': 'Squid Game',
                'description': 'Creative graphic design inspired by Squid Game.',
                'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/7210e8218551427.67a34fac9e431.jpg',
                'link': 'https://www.behance.net/gallery/218551427/Squid-Game'
            },
            {
                'name': 'Pathao Login Page',
                'description': 'UI design for Pathao login page.',
                'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/8017b1217267011.Y3JvcCw4MDgsNjMyLDAsMA.jpg',
                'link': 'https://www.behance.net/gallery/217267011/Pathao-Login-page'
            },
            {
                'name': '3D Photo Manipulation',
                'description': 'Advanced 3D photo manipulation using Photoshop.',
                'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/7fec12215788441.Y3JvcCwxODA2LDE0MTMsMTYwLDA.jpg',
                'link': 'https://www.behance.net/gallery/215788441/3D-Photo-Manipulation'
            },
            {
                'name': 'Christmas Banner',
                'description': 'Festive Christmas banner design.',
                'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/b23397215787261.Y3JvcCwxMTA0LDg2NCwxMTc1LDA.png',
                'link': 'https://www.behance.net/gallery/215787261/Christmas-Banner'
            },
            {
                'name': 'T-Shirt Design',
                'description': 'Creative T-shirt graphic design.',
                'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/7a39d5215787851.Y3JvcCwxNTM0LDEyMDAsMTkzLDA.jpg',
                'link': 'https://www.behance.net/gallery/215787851/T-Shirt-Design'
            },
            {
                'name': 'Photo Manipulation',
                'description': 'Creative photo manipulation artwork.',
                'image': 'https://mir-s3-cdn-cf.behance.net/projects/404/7ffe65215787711.Y3JvcCwxNTM0LDEyMDAsMzQsMA.jpg',
                'link': 'https://www.behance.net/gallery/215787711/Photo-Manipulation'
            },
        ],
        'social': {
            'facebook': 'http://facebook.com/PaveLRahmaN25',
            'behance': 'https://www.behance.net/pavelrahman9',
        }
    }
    return render(request, 'home.html', context)