module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                myGreen: {
                    100: '#92E591',
                    200: '#8AD789',
                    300: '#81C880',
                    400: '#79BA78',
                    500: '#71AC70       ',
                    600: '#699E68',
                    700: '#608F5F',
                    800: '#588157',
                },
                myWhite: {
                    50: '#fff',
                    100: '#F3F3F3',
                    200: '#E6E6E6',
                    300: '#DADADA',
                    400: '#CDCDCD',
                    500: '#C1C1C1',
                    600: '#B4B4B4',
                    700: '#A8A8A8',
                    800: '#9B9B9B',
                    900: '#000'
                },
                myRed: {
                    100: '#FFDBDB',
                    200: '#FFB6B6',
                    300: '#FF9292',
                    400: '#FF6D6D',
                    500: '#FF4949',
                    600: '#FF4949',
                    700: '#FF2424',
                    800: '#FF0000',
                },
                myBlue: {
                    100: '#DBDBFF',
                    200: '#B6B6FF',
                    300: '#9292FF',
                    400: '#6D6DFF',
                    500: '#4949FF',
                    600: '#4949FF',
                    700: '#2424FF',
                    800: '#0000FF',
                },
            }
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
