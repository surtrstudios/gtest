{
    'variables': {
        'library%': 'static_library',
    },

    'targets': [
        {
            'target_name':  'gtest',
            'type': '<(library)',

            'sources': [
                'src/gtest-all.cc'
            ],

            'defines+': [ '_VARIADIC_MAX=10' ],

            'include_dirs': [
                '../gtest',
                '../gtest/include'
            ],

            'direct_dependent_settings': {
                'include_dirs': [
                    '../gtest',
                    '../gtest/include'
                ],
                'defines+': [ '_VARIADIC_MAX=10' ],
            },
        },
        {
            'target_name': 'gtest_main',
            'type': '<(library)',

            'sources': [
                'src/gtest_main.cc'
            ],

            'defines+': [ '_VARIADIC_MAX=10' ],

            'dependencies': [
                'gtest',
            ],
            
            'include_dirs': [
                '../gtest',
                '../gtest/include'
            ],

            'direct_dependent_settings': {
                'include_dirs': [
                    '../gtest',
                    '../gtest/include'
                ],
                'defines+': [ '_VARIADIC_MAX=10' ],
            },
        }
    ]
}