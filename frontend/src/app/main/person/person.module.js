(function(){
  'use strict';
  var serverUrl = config_data.protocol + config_data.address + ':' + config_data.port + '/'
  var urlPerson = serverUrl + 'api/person/'

  angular
    .module('app.person', ['app.pages.auth.login'])
    .config(config)
    .constant('personApi', urlPerson)



  function config($stateProvider, msApiProvider, msNavigationServiceProvider) {
    
    $stateProvider
      .state('app.person', {
        abstract: true,
        resolve: {
          is_logged : function(AuthServices){
            return AuthServices.check()
          }
        }
      })

      .state('app.person.list', {
        url: '/person',
        views: {
            'content@app': {
                templateUrl: '/app/main/person/person.list.html',
                controller: 'PersonController',
                controllerAs: 'person',
            }
        },
        resolve: {
          persons : function(PersonServices, is_logged){
            return PersonServices.load()
          }
        }
      })
      .state('app.person.form', {
        url: '/form/:id',
        views: {
            'content@app': {
                templateUrl: '/app/main/person/person.form.html',
                controller: 'PersonFormController',
                controllerAs: 'form',
            }         
        },
        resolve: {
          person: function(PersonServices, $stateParams){
              return PersonServices.get($stateParams.id)
          }
        }
      })

      msNavigationServiceProvider.saveItem('fuse.sample', {
        title    : 'Person',
        icon     : 'icon-user',
        state    : 'app.person',
        /*stateParams: {
            'param1': 'page'
         },*/
        weight   : 1
      });
  }
})();
