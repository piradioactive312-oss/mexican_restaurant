import os

header = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu - Authentic Mexican Flavors</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'mex-yellow': '#FFB200',
                        'mex-green': '#015536',
                        'mex-red': '#F52F1B',
                        'mex-dark': '#1B1B1B',
                    },
                    fontFamily: {
                        display: ['Caprasimo', 'cursive'],
                        sans: ['Ruda', 'sans-serif'],
                        body: ['Montserrat', 'sans-serif'],
                    },
                    boxShadow: {
                        'card': '-10.276px 10.276px 0 0 #D72022',
                        'circle': '0 15px 25px -5px rgba(0, 0, 0, 0.2)',
                    }
                }
            }
        }
    </script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Ruda:wght@400;700;900&family=Caprasimo&display=swap" rel="stylesheet">
    <!-- Phosphor Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="stylesheet" href="style.css">
</head>

<body class="font-body text-mex-dark bg-white antialiased overflow-x-hidden">

    <!-- Yellow Hero Section -->
    <section class="relative bg-mex-yellow flex flex-col items-center justify-start pb-20 z-10">
        
        <!-- Navegação (Solid Background variant) -->
        <header class="w-full max-w-7xl mx-auto px-6 py-6 flex justify-between items-center z-20">
            <!-- Logo -->
            <a href="index.html" class="flex items-center gap-3">
                <img src="assets/img/logo.svg" alt="The Authentic Mexican Flavors Logo" class="h-14 md:h-16 object-contain">
            </a>

            <!-- Desktop Nav -->
            <nav class="hidden md:flex items-center gap-8">
                <a href="index.html#menu" class="text-white font-sans font-bold uppercase text-sm tracking-widest hover:text-white/80 transition-colors">Menu</a>
                <a href="index.html#about" class="text-white font-sans font-bold uppercase text-sm tracking-widest hover:text-white/80 transition-colors">About Us</a>
                <a href="index.html#ratings" class="text-white font-sans font-bold uppercase text-sm tracking-widest hover:text-white/80 transition-colors">Ratings</a>
                <a href="index.html#find-us" class="text-white font-sans font-bold uppercase text-sm tracking-widest hover:text-white/80 transition-colors">Find Us</a>
            </nav>

            <!-- Mobile Menu Button -->
            <button class="md:hidden text-white text-3xl hover:text-white/80 transition-colors" aria-label="Open Menu">
                <i class="ph-bold ph-list"></i>
            </button>
        </header>"""

footer = """
    <!-- Footer -->
    <footer class="bg-mex-green text-white pt-20 pb-8 px-6 mt-12">
        <div class="max-w-6xl mx-auto grid grid-cols-3 gap-4 md:gap-8 mb-16 text-left">
            <!-- Links -->
            <div>
                <h4 class="font-sans font-bold text-sm md:text-lg mb-4 md:mb-6 tracking-wider uppercase">Links</h4>
                <ul class="font-body space-y-3 md:space-y-4 text-xs md:text-sm text-gray-200">
                    <li><a href="index.html#menu" class="hover:text-mex-yellow transition-colors block">Menu</a></li>
                    <li><a href="index.html#contact" class="hover:text-mex-yellow transition-colors block">Contact</a></li>
                    <li><a href="index.html#about" class="hover:text-mex-yellow transition-colors block">About Us</a></li>
                    <li><a href="index.html#ratings" class="hover:text-mex-yellow transition-colors block">Ratings</a></li>
                    <li><a href="index.html#find-us" class="hover:text-mex-yellow transition-colors block">Location & Hours</a></li>
                </ul>
            </div>

            <!-- Legal -->
            <div>
                <h4 class="font-sans font-bold text-sm md:text-lg mb-4 md:mb-6 tracking-wider uppercase">Legal</h4>
                <ul class="font-body space-y-3 md:space-y-4 text-xs md:text-sm text-gray-200">
                    <li><a href="#" class="hover:text-mex-yellow transition-colors block">Privacy Policy</a></li>
                    <li><a href="#" class="hover:text-mex-yellow transition-colors block">Terms of Use</a></li>
                </ul>
            </div>

            <!-- Follow Us -->
            <div class="flex flex-col items-start">
                <h4 class="font-sans font-bold text-sm md:text-lg mb-4 md:mb-6 tracking-wider uppercase">Follow Us</h4>
                <div class="flex flex-nowrap gap-1.5 md:gap-4">
                    <a href="#" class="hover:-translate-y-1 transform transition-transform duration-300">
                        <img src="assets/img/icon-youtube.svg" alt="YouTube" class="w-6 h-6 md:w-10 md:h-10 object-contain shrink-0">
                    </a>
                    <a href="#" class="hover:-translate-y-1 transform transition-transform duration-300">
                        <img src="assets/img/icon-instagram.svg" alt="Instagram" class="w-6 h-6 md:w-10 md:h-10 object-contain shrink-0">
                    </a>
                    <a href="#" class="hover:-translate-y-1 transform transition-transform duration-300">
                        <img src="assets/img/icon-facebook.svg" alt="Facebook" class="w-6 h-6 md:w-10 md:h-10 object-contain shrink-0">
                    </a>
                </div>
            </div>
        </div>

        <!-- Copyright -->
        <div class="max-w-6xl mx-auto border-t border-white/20 pt-8 text-center">
            <p class="font-body text-sm text-gray-300 font-medium tracking-wide">
                Website developed by <a href="#" class="text-white hover:text-mex-yellow underline decoration-gray-400 underline-offset-4 transition-colors">Pedro Sampaio</a>
            </p>
        </div>
    </footer>

    <!-- Script Customizado -->
    <script src="script.js"></script>
</body>
</html>"""

def make_page(filename, title, subtitle, categories):
    html = header + f"""
        <!-- Hero Content -->
        <div class="relative w-full max-w-4xl mx-auto flex flex-col items-center justify-center pt-8 md:pt-16 pb-12 px-6">
            <div class="absolute inset-0 flex items-center justify-center opacity-10 pointer-events-none">
                <img src="assets/img/icon-taco.svg" alt="Background" class="w-64 h-64 md:w-96 md:h-96 object-contain">
            </div>
            
            <h1 class="font-sans font-black text-mex-green text-5xl md:text-6xl text-center uppercase tracking-wide relative z-10">
                {title}
            </h1>
            <p class="font-body text-mex-dark text-center mt-4 text-base md:text-lg max-w-lg relative z-10 font-medium">
                {subtitle}
            </p>
        </div>

        <!-- Borda Arredondada (Scalloped) apontando para baixo -->
        <div class="absolute bottom-0 left-0 w-full h-[20px] transform translate-y-[calc(100%-1px)]"
            style="background-image: radial-gradient(circle at 50% 0, #FFB200 20px, rgba(255, 178, 0, 0) 20.5px); background-size: 40px 20px; background-repeat: repeat-x;">
        </div>
    </section>

    <!-- Menu Details Content -->
    <main class="py-24 bg-white px-6">
        <div class="max-w-5xl mx-auto">
"""
    for cat in categories:
        html += f"""
            <div class="flex items-center justify-center gap-4 md:gap-8 mb-12 mt-16 first:mt-0">
                <img src="assets/img/red-ornament.svg" alt="" class="h-6 md:h-8 object-contain">
                <h2 class="font-sans font-black text-xl md:text-3xl text-mex-dark uppercase tracking-widest text-center whitespace-nowrap">{cat['title']}</h2>
                <img src="assets/img/red-ornament.svg" alt="" class="h-6 md:h-8 object-contain transform rotate-180">
            </div>
            {cat['desc'] if 'desc' in cat else ''}
            <div class="grid grid-cols-1 md:grid-cols-2 gap-x-16 gap-y-8 mb-24">
"""
        for item in cat['items']:
            desc_html = f'<span class="font-body text-xs text-gray-500 mt-1 font-medium">{item["desc"]}</span>' if 'desc' in item else ''
            html += f"""
                <div class="flex flex-col">
                    <div class="flex items-baseline w-full">
                        <span class="font-sans font-bold text-mex-dark uppercase tracking-wide text-sm md:text-base">{item['name']}</span>
                        <div class="flex-grow border-b-2 border-dotted border-mex-red mx-4 relative top-[-4px]"></div>
                        <span class="font-sans font-black text-mex-dark md:text-lg">{item['price']}</span>
                    </div>
                    {desc_html}
                </div>
"""
        html += """
            </div>
"""
    html += """
        </div>
    </main>
"""
    html += footer
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


# 1. DRINKS
make_page("menu-drinks.html", "Drinks", "Refreshments to perfectly complement your authentic meal.", [
    {
        "title": "Cold Drinks",
        "items": [
            {"name": "Jugos Naturales", "price": "From $4", "desc": "Agua de Jamaica, Tamarindo ou Horchata &bull; 16oz $4.00 &bull; 32oz $7.00"},
            {"name": "Jugo de Naranja", "price": "$8.00", "desc": "Suco de Laranja Natural &bull; 16oz"},
            {"name": "Smoothies", "price": "$7.00", "desc": "Morango, Banana, Manga ou Papaia &bull; 16oz"},
            {"name": "Batido Mixto Mix", "price": "$9.00", "desc": "16oz"},
            {"name": "Boing", "price": "$3.50", "desc": "Suco Mexicano"},
            {"name": "Jarritos", "price": "$3.50", "desc": "Refrigerante Mexicano"},
            {"name": "Domestic Soft Drinks", "price": "$2.50", "desc": "Refrigerantes Nacionais / Água"},
            {"name": "Seltzer Water", "price": "$2.50", "desc": "Água Gaseificada"},
            {"name": "Snapple", "price": "$3.50"},
            {"name": "Mexican Coca-Cola", "price": "$3.75"}
        ]
    },
    {
        "title": "Hot Drinks",
        "items": [
            {"name": "Champurrado", "price": "$5.00", "desc": "Bebida espessa de chocolate"},
            {"name": "Coffee", "price": "$4.00", "desc": "Café"},
            {"name": "Cappuccino", "price": "$5.00"},
            {"name": "Espresso", "price": "$4.00"},
            {"name": "Tea", "price": "$3.00", "desc": "Chá"},
            {"name": "Chocolate Quente", "price": "$5.00"},
            {"name": "Arroz con Leche", "price": "$5.00", "desc": "Arroz Doce - servido como bebida quente"}
        ]
    }
])


# 2. SANDWICHES
make_page("menu-sandwiches.html", "Mexican Sandwiches", "Traditional Tortas and Cemitas crafted with the finest ingredients.", [
    {
        "title": "Mexican Sandwiches",
        "desc": '<p class="text-center font-body text-gray-500 mb-8 font-medium">Os preços variam entre o formato Torta e o formato Cemita.</p>',
        "items": [
            {"name": "Pollo (Frango)", "price": "From $12", "desc": "Torta $12.00 &bull; Cemita $15.00"},
            {"name": "Milanesa de Pollo", "price": "From $12", "desc": "Torta $12.00 &bull; Cemita $15.00"},
            {"name": "Jamón con Queso Oaxaca", "price": "From $12", "desc": "Presunto e Queijo &bull; Torta $12.00 &bull; Cemita $15.00"},
            {"name": "Cecina", "price": "From $12", "desc": "Carne Seca/Curada &bull; Torta $12.00 &bull; Cemita $15.00"},
            {"name": "Huevo & Chorizo", "price": "From $12", "desc": "Ovo e Linguiça &bull; Torta $12.00 &bull; Cemita $15.00"},
            {"name": "Carnitas", "price": "From $12", "desc": "Porco Cozido &bull; Torta $12.00 &bull; Cemita $15.00"},
            {"name": "Pastor", "price": "From $12", "desc": "Porco Marinado &bull; Torta $12.00 &bull; Cemita $15.00"},
            {"name": "Carne Enchilada", "price": "From $13", "desc": "Porco Apimentado &bull; Torta $13.00 &bull; Cemita $15.00"},
            {"name": "Bistec / Milanesa de Res", "price": "From $13", "desc": "Carne de Boi &bull; Torta $13.00 &bull; Cemita $15.00"},
            {"name": "Torta de Birria", "price": "From $13", "desc": "Torta $13.00 &bull; Cemita $16.00"}
        ]
    }
])


# 3. STARTERS, SALADS, SOUPS
make_page("menu-starters.html", "Starters, Salads & Soups", "The perfect way to begin your Authentic Mexican journey.", [
    {
        "title": "Starters",
        "items": [
            {"name": "Guacamole", "price": "From $7", "desc": "Pequeno $7.00 &bull; Grande $15.00"},
            {"name": "Nachos", "price": "$11.00"},
            {"name": "Flautas", "price": "$16.00"},
            {"name": "Tamales", "price": "From $4", "desc": "1 por $4.00 &bull; 6 por $22.00 &bull; 12 por $42.00"},
            {"name": "Queso Fundido con Chorizo", "price": "$14.00"},
            {"name": "Nachos Mi Pequeño Mexico", "price": "$14.00"}
        ]
    },
    {
        "title": "Salads",
        "items": [
            {"name": "Ensalada de Aguacate", "price": "$13.00", "desc": "Abacate"},
            {"name": "Ensalada de Pollo", "price": "$14.00", "desc": "Frango"},
            {"name": "Ensalada de Pollo y Aguacate", "price": "$16.00"},
            {"name": "Nopales", "price": "$13.00", "desc": "Salada de Cacto"},
            {"name": "Ensalada de la Casa", "price": "$8.00"}
        ]
    },
    {
        "title": "Soups",
        "items": [
            {"name": "Pollo (Canja de Frango)", "price": "From $6", "desc": "Pequena $6.00 &bull; Grande $8.00"},
            {"name": "Pozole Tradicional", "price": "From $11", "desc": "Pequena $11.00 &bull; Grande $15.00"},
            {"name": "Pancita", "price": "From $13", "desc": "Sopa de Dobradinha &bull; Pequena $13.00 &bull; Grande $16.00"},
            {"name": "Caldo de Pollo con Chile Guajillo", "price": "From $9", "desc": "Pequeno $9.00 &bull; Grande $14.00"},
            {"name": "Caldo de Res", "price": "From $12", "desc": "Sopa de Carne &bull; Pequeno $12.00 &bull; Grande $18.00"},
            {"name": "Sopa de Tortilla", "price": "From $7", "desc": "Pequena $7.00 &bull; Grande $13.00"}
        ]
    }
])
