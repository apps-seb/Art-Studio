const fs = require('fs');

let index = fs.readFileSync('index.html', 'utf8');

// Modificar CSS de Ruleta
index = index.replace(/\.swiper-ruleta \{[^}]+\}/, '.swiper-ruleta { width: 100%; padding-top: 50px; padding-bottom: 50px; z-index: 10; overflow: visible; }');
index = index.replace(/\.swiper-slide-ruleta \{[^}]+\}/, '.swiper-slide-ruleta { width: 260px; height: 380px; background-color: #EAE5DF; border-radius: 8px; overflow: hidden; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6); display: flex; flex-direction: column; transition: filter 0.5s ease; filter: brightness(0.4); border: 1px solid rgba(200, 169, 126, 0.2); }');
index = index.replace(/\.swiper-slide-ruleta-active \{[^}]+\}/, '.swiper-slide-ruleta-active { filter: brightness(1); border-color: rgba(200, 169, 126, 0.6); }');
index = index.replace(/\.ruleta-img-wrapper \{[^}]+\}/, '.ruleta-img-wrapper { height: 75%; overflow: hidden; }');
index = index.replace(/\.ruleta-info \{[^}]+\}/, '.ruleta-info { height: 25%; padding: 15px; display: flex; flex-direction: column; justify-content: center; background-color: #0F3B2F; color: #EAE5DF; text-align: center; }');

// Modificar HTML de Ruleta
const oldRuletaHTML = `<section id="ruleta" class="relative w-full h-screen overflow-hidden flex items-center bg-forest">
                <div class="ruleta-bg-container" id="ruleta-bg-container">
                    <!-- Imágenes de fondo dinámicas -->
                </div>
                <div class="ruleta-bg-overlay"></div>

                <div class="absolute top-16 left-8 md:left-24 z-20 pointer-events-none">
                    <p class="font-sans text-champagne text-xs tracking-[0.3em] uppercase mb-4">Colección Rotativa</p>
                    <h2 class="font-serif text-5xl md:text-7xl text-beige overflow-hidden">
                        <span class="block translate-y-[100%] ruleta-title-anim" id="ruleta-title">Obra Principal</span>
                    </h2>
                    <p class="font-sans text-sm tracking-widest text-champagne mt-4 uppercase opacity-0 ruleta-author-anim" id="ruleta-author">Autor Desconocido</p>
                </div>

                <div class="w-full md:w-1/2 ml-auto h-full relative z-10 flex items-center justify-center">
                    <div class="swiper swiper-ruleta cursor-swiper">
                        <div class="swiper-wrapper" id="ruleta-wrapper">
                            <!-- Las tarjetas se generarán dinámicamente -->
                        </div>
                    </div>
                </div>
                <div class="absolute bottom-16 left-8 md:left-24 z-20 flex gap-4">
                    <button class="w-12 h-12 rounded-full border border-champagne text-champagne flex items-center justify-center hover:bg-champagne hover:text-forest transition-colors hover-target ruleta-prev pointer-events-auto cursor-pointer relative z-30">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7"></path></svg>
                    </button>
                    <button class="w-12 h-12 rounded-full border border-champagne text-champagne flex items-center justify-center hover:bg-champagne hover:text-forest transition-colors hover-target ruleta-next pointer-events-auto cursor-pointer relative z-30">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                    </button>
                </div>
            </section>`;

const newRuletaHTML = `<section id="ruleta" class="relative w-full min-h-screen overflow-hidden flex flex-col md:flex-row items-center bg-forest py-20 md:py-0">
                <div class="ruleta-bg-container" id="ruleta-bg-container">
                    <!-- Imágenes de fondo dinámicas -->
                </div>
                <div class="ruleta-bg-overlay"></div>

                <div class="w-full md:w-1/2 px-8 md:px-24 z-20 flex flex-col justify-center pointer-events-none mt-16 md:mt-0 relative">
                    <p class="font-sans text-champagne text-xs tracking-[0.3em] uppercase mb-4">Colección Rotativa</p>
                    <h2 class="font-serif text-5xl md:text-7xl text-beige overflow-hidden">
                        <span class="block translate-y-[100%] ruleta-title-anim" id="ruleta-title">Obra Principal</span>
                    </h2>
                    <p class="font-sans text-sm tracking-widest text-champagne mt-4 uppercase opacity-0 ruleta-author-anim" id="ruleta-author">Autor Desconocido</p>

                    <div class="mt-8 md:mt-12 flex gap-4 pointer-events-auto">
                        <button class="w-12 h-12 rounded-full border border-champagne text-champagne flex items-center justify-center hover:bg-champagne hover:text-forest transition-colors hover-target ruleta-prev cursor-pointer relative z-30" aria-label="Anterior">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                        </button>
                        <button class="w-12 h-12 rounded-full border border-champagne text-champagne flex items-center justify-center hover:bg-champagne hover:text-forest transition-colors hover-target ruleta-next cursor-pointer relative z-30" aria-label="Siguiente">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                        </button>
                    </div>
                </div>

                <div class="w-full md:w-1/2 w-full h-full relative z-10 flex items-center justify-center mt-12 md:mt-0 overflow-hidden">
                    <div class="swiper swiper-ruleta cursor-swiper">
                        <div class="swiper-wrapper" id="ruleta-wrapper">
                            <!-- Las tarjetas se generarán dinámicamente -->
                        </div>
                    </div>
                </div>
            </section>`;

index = index.replace(oldRuletaHTML, newRuletaHTML);

// Modificar JS de Ruleta
index = index.replace(/direction: 'vertical'/, "direction: 'horizontal'");
// Ajustar effect de coverflow para horizontal
index = index.replace(/coverflowEffect: \{ rotate: 20, stretch: 0, depth: 300, modifier: 1, slideShadows: false \}/, "coverflowEffect: { rotate: 0, stretch: 60, depth: 200, modifier: 1, slideShadows: false }");

// Ajustar ruleta-info a un diseño más elegante
index = index.replace(/<div class="ruleta-info">\s*<h4 class="font-serif text-2xl text-champagne italic">\$\{item\.title\}<\/h4>\s*<p class="font-sans text-xs tracking-widest mt-2 uppercase">\$\{item\.year\}<\/p>\s*<\/div>/g,
`<div class="ruleta-info">
                    <h4 class="font-serif text-xl md:text-2xl text-champagne italic leading-none">\${item.title}</h4>
                    <p class="font-sans text-[10px] md:text-xs tracking-widest mt-2 uppercase text-beige opacity-80">\${item.year}</p>
                </div>`);

fs.writeFileSync('index.html', index);
