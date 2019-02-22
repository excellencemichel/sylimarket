 $(document).ready(function(){


        function refreshHome(){
          console.log("In home")
          var productHome = $(".product-home")
          var productHomeItem = productHome.find(".product-home-item")
        var productUpdateform = productHomeItem.find(".product-update-form")

        var refreshProductUrl = "/api/product/"
        var refreshProductMethod = "GET"
        var data = {}

        $.ajax({
          url: refreshProductUrl,
          method: refreshProductMethod,
          data: data,
          success: function(data){
            var hiddenProductAddForm = $(".product-item-add-form")
            var hiddenProductRemoveForm = $(".product-item-remove-form")
            if(data.products.length > 0){
              productUpdateform.html(" ")

              $.each(data.products, function(index, value){
                console.log("Dans le cart: ", value.in_cart)
                if(value.in_cart==false){
                var newProductAddForm = hiddenProductAddForm.clone()
                newProductAddForm.css("display", "inline-block")
                newProductAddForm.find(".cart-item-product-id").val(value.id)

                productUpdateform.prepend(newProductAddForm.html())


                }

                else if (value.in_cart==true){
                  var newProductRemoveForm = hiddenProductRemoveForm.clone()
                  newProductRemoveForm.css("display", "inline-block")
                  newProductRemoveForm.find(".cart-item-product-id").val(value.id)

                  productUpdateform.prepend(newProductRemoveForm.html())
                }


              })
            }

          },

          error: function(){
            $.alert({
                title: "oops !",
                content: "Une erreur s'est occasionée",
                theme: "modern",
              })
          }

        })
        }

      var productForm = $(".form-product-ajax")
      productForm.submit(function(event){
          event.preventDefault()
          var thisForm = $(this)
          // var actionEndpoint = thisForm.attr("action")
          var actionEndpoint = thisForm.attr("data-endpoint")
          var httpMethod = thisForm.attr("method")
          var formData = thisForm.serialize();
          $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function(data){
              var submitSapn = thisForm.find(".submit-span")
              if (data.added){
                submitSapn.html("<a href='{% url 'carts:checkout' %}' class='btn btn-primary' style='margin: 7px;'><i class='fa fa-shopping-cart inner-right-vs'>VOIR DANS LE PANIER</i></a>|<button type='submit' class='btn btn-primary' style='margin: 7px;'><i class='fa fa-shopping-cart inner-right-vs'></i>ENLEVER DU PANIER</a>")
              }
              else{
                submitSapn.html("<button type='submit' class='btn btn-primary'><i class='fa fa-shopping-cart inner-right-vs'></i>PAYER MAINTENANT</button>")
              }

              var navBarCount = $(".navbar-cart-count")
              navBarCount.text(data.cartItemsCount)
              var currentPath = window.location.href
              // if(currentPath.indexOf("") != -1){
              //   refreshHome()
              // }
              if(currentPath.indexOf("cart") != -1){
                refreshCart()
              }
            },

            error: function(errorData){
              $.alert({
                title: "oops !",
                content: "Une erreur s'est occasionée",
                theme: "modern",
              })
            }
          })
      })

      function refreshCart(){
        console.log("In current cart")
        var cartTableHomeSomme = $(".cart-table-home-somme")
        var cartTableHome = $(".cart-table-home")
        var cartBodyHome = cartTableHome.find(".cart-body-home")
        var productRows = cartBodyHome.find(".cart-product-home")
        var currentUrl = window.location.href

        var refreshCartUrl = "/cart/api/cart/"
        var refreshCartMethod = "GET"
        var data = {}
        $.ajax({
          url : refreshCartUrl,
          method: refreshCartMethod,
          data: data,
          success : function(data){
            var hiddenCartRemoveForm = $(".cart-item-remove-form")
            if(data.products.length > 0){

            productRows.html(" ")
            i = 1
            $.each(data.products, function(index, value){
              var newCartItemRemove = hiddenCartRemoveForm.clone()
              newCartItemRemove.css("display", "block")
              newCartItemRemove.find(".cart-item-product-id").val(value.id)
              cartBodyHome.prepend("<tr><td class='romove-item'>" + newCartItemRemove.html() + " <td class='cart-image'><a class='entry-thumbnail' href='" + value.url +"'><img src=\"{% static 'images/products/p1.jpg' %}\" alt=''></a></td><td class='cart-product-name-info'><h4 class='cart-product-description'><a href='" + value.url + "'>" + value.name + "</a></h4><div class='row'><div class='col-sm-4'><div class='rating rateit-small'></div></div><div class='col-sm-8'><div class='reviews'>(06 Reviews)</div></div></div><div class='cart-product-info'><span class='product-color'>COLOR:<span>Blue</span></span></div></td><td class='cart-product-edit'><a href='#' class='product-edit'>Edit</a></td><td class='cart-product-quantity'><div class='quant-input'><div class='arrows'><div class='arrow plus gradient'><span class='ir'><i class='icon fa fa-sort-asc'></i></span></div><div class='arrow minus gradient'><span class='ir'><i class='icon fa fa-sort-desc'></i></span></div></div><input type='text' value='1'></div></td><td class='cart-product-sub-total'><span class='cart-sub-total-price'>$" + value.price + "</span></td><td class=cart-product-grand-total><span class=cart-grand-total-price>$" + value.price + "</span></td></tr> " )

            })

            cartTableHomeSomme.find(".cart-subtotal-home-somme").text(data.subtotal)
            cartTableHomeSomme.find(".cart-total-home-somme").text(data.total)
            console.log("Seperieur 0")
            totalText = cartBodyHome.find(".cart-total-home").text()
            console.log("Voici le total", data.total)

            }
            else{
              window.location.href = currentUrl
              console.log("inferieur à 0")
            }
            console.log("success")

            console.log(data)

          },

          error: function(errorData){
              $.alert({
                title: "oops !",
                content: "Une erreur s'est occasionée",
                theme: "modern",
              })
          }
        })

      }










       var payementMethodContainer = $(".checkout-step-01")
       var payementMethodForm = payementMethodContainer.find("#collapseOne")
       var payementMethodLink = payementMethodForm.find(".payement-method-link")
       var billingContainer = $(".checkout-step-02")
       var billinForm = billingContainer.find("#collapseTwo")
       var billinLink = billinForm.find(".billing-link")
       console.log()


       var payementForm = $(".payement-choice-form")

      payementForm.submit(function(event){
        event.preventDefault()
        var inputs = payementForm.find("input")
        var payementMethodChoice = payementForm.find("[name='payementmethod']")
        // console.log("La valeur est:", payementMethodChoice.checked)


        var hiddenFacturationlivraison = $(".payement-method-livraison")
        var hiddenFacturationBancaire = $(".payement-method-bancaire")
        var hiddenFacturationMobile = $(".payement-method-mobile")
        var facturationAddress = $(".facturation-address")
        
        facturationAddress.html(" ")
        $.each(payementMethodChoice, function(index,choix){
          if (choix.checked){
            payementMethodForm.removeClass("in")
            payementMethodLink.addClass("collapsed")
            billinForm.addClass("in")
            billinLink.removeClass("collapsed")
            console.log("Un choix")
            console.log(choix.value)
            if(choix.value == "livraison"){
            
                var newFacturationLivraisonForm = hiddenFacturationlivraison.clone()
                newFacturationLivraisonForm.css("display", "block")


                facturationAddress.prepend(newFacturationLivraisonForm.html())
            }

            else if(choix.value == "bancaire"){
                var newFacturationBancaireForm = hiddenFacturationBancaire.clone()
                newFacturationBancaireForm.css("display", "block")

                facturationAddress.prepend(newFacturationBancaireForm.html())
            }

            else if(choix.value == "mobile"){
                var newFacturationMobileForm = hiddenFacturationMobile.clone()
                newFacturationMobileForm.css("display", "block")


                facturationAddress.prepend(newFacturationMobileForm.html())

              }

              else{
                alert("Vous devez faire un choix de payement !")
              }



          }
          else if(!choix.checked){
            console.log("Pas de choix")

          }


        })


      })
 



  })


