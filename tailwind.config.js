module.exports = {
    purge: {
      enabled: true,
      content: [
        './thor_controller/src/**/*.js',
        './thor_controller/src/**/*.jsx'
      ],
      options: {
        whitelist: []
      }
    },
    darkMode: false, // or 'media' or 'class'
    theme: {
      colors: {
        django: '#092e20',
        react: '#61DBFB',
        tailwind: '#00b4b6'
      }
    },
    variants: {
      extend: {},
    },
    plugins: [],
  }
  