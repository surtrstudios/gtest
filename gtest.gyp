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

            'include_dirs': [
                '../gtest',
                '../gtest/include'
            ],

            'direct_dependent_settings': {
                'include_dirs': [
                    '../gtest',
                    '../gtest/include'
                ],
            },
        },
        {
            'target_name': 'gtest_main',
            'type': '<(library)',

            'sources': [
                'src/gtest_main.cc'
            ],

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
            },
        }
    ]
}