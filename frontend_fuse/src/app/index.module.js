(function ()
{
    'use strict';

    /**
     * Main module of the Fuse
     */
    angular
        .module('fuse', [

            // Core
            'app.core',

            // Navigation
            'app.navigation',

            // Toolbar
            'app.toolbar',

            // Quick Panel
            'app.quick-panel',

            'app.pages.auth.login',

            // Sample
            'app.sample',

            // Person
            'app.person',

            // localStorage
            'LocalStorageModule',

            // DataTables
            'datatables'
        ]);
})();
