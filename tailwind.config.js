/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
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
    },
  },
  plugins: [],
}
