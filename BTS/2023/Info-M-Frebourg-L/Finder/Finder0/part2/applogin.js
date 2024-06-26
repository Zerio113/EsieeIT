//applogin.js
var app = new Vue({
    el: '#vueapplogin',
    data:{
        successMessage: "Bien joué",
        errorMessage: "Raté ( you can use root / root )",
        logDetails: {username: '', password: ''},
    },
 
    methods:{
        keymonitor: function(event) {
            if(event.key == "Enter"){
                app.checkLogin();
            }
        },
 
        checkLogin: function(){
            var logForm = app.toFormData(app.logDetails);
            axios.post('login.php', logForm)
                .then(function(response){
 
                    if(response.data.error){
                        app.errorMessage = response.data.message;
                    }
                    else{
                        app.successMessage = response.data.message;
                        app.logDetails = {username: '', password:''};
                        setTimeout(function(){
                            window.location.href="chambre.php";
                        },2000);
                         
                    }
                });
        },
 
        toFormData: function(obj){
            var form_data = new FormData();
            for(var key in obj){
                form_data.append(key, obj[key]);
            }
            return form_data;
        },
 
        clearMessage: function(){
            app.errorMessage = '';
            app.successMessage = '';
        }
 
    }
});


