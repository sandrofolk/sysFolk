(function ()
{
    'use strict';

    angular
        .module('app.pages.auth.login')
        .controller('LoginController', LoginController);

    /** @ngInject */
    function LoginController(AuthServices, $state)
    {
        var vm = this

        vm.signIn = function(){
            AuthServices.signIn(vm.form)
            .then(
                function(response){
                    $state.go('app.person.list')
                },
                function(error){
                    swal({
                        title: 'Ops!',
                        text: error.data.non_field_errors[0],
                        type: 'error'
                    })
                }
            )
        }
    }
})();