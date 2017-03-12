(function ()
{
    'use strict';

    angular
        .module('fuse')
        .config(config)
        .factory('tokenInterceptor', tokenInterceptor)
  
    function tokenInterceptor($q, localStorageService, $injector){
        return {
            request: function(config) {
                var token = localStorageService.get('token')
                if (token) {
                    config.headers['Authorization'] = 'Token ' + token;
                }
                return config;
            },
            responseError: function(response) {
                // Caso nao retorne nada esta em manutencao
                // if(response.status <= 0) {
				// 	$injector.get('$state').go('app.pages_maintenance')
                //     return $q.reject(response);
                // }

				// if(response.status == 500) {
				// 	$injector.get('$state').go('app.pages_errors_error-500')
                //     return $q.reject(response);
                // }

                // Caso nao esteja logado
                if (response.status === 401) {
                    
					$injector.get('$state').go('app.pages_auth_login')
					$injector.get('AuthServices').signOut()
					return $q.reject(response)
                }
                return $q.reject(response)
            }
        }
    }


    /** @ngInject */
    function config($translateProvider, $httpProvider)
    {
        // Put your common app configurations here
            $httpProvider.interceptors.push('tokenInterceptor')


        // angular-translate configuration
        $translateProvider.useLoader('$translatePartialLoader', {
            urlTemplate: '{part}/i18n/{lang}.json'
        });
        $translateProvider.preferredLanguage('en');
        $translateProvider.useSanitizeValueStrategy('sanitize');
    }

})();