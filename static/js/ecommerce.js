 $(document).ready(function(){


    
  // Auto Search

  var searForm = $(".query-search-form")

  var searchInput = searForm.find("[name='q']") // input name='q'

  var typingTimer;
  var typingInterval = 500 // 
  var searchBtn = searForm.find("[type='submit']")

  searchInput.keyup(function(event){
    //key released
    clearTimeout(typingTimer)

    typingTimer = setTimeout(perforSearch, typingInterval)
    
    
  })

  searchInput.keydown(function(event){
    // key pressed
    clearTimeout(typingTimer)
  })

  function displaySearching(){
    searchBtn.addClass("disabled")
    searchBtn.html("<i class='fa fa-spin fa-spinner'></i> Searching...")
  }

  function perforSearch(){
    displaySearching()
    var query = searchInput.val()

    setTimeout(function(){

    window.location.href="/search/?q=" + query
    }, 1000)
  }


        // Stat Add update
      var productFormAdd = $(".form-product-ajax-add")
      productFormAdd.submit(function(event){
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
              var submitSpan = thisForm.find(".submit-span")
              if (data.added){
                submitSpan.html("<a href='/cart' class='btn btn-primary' style='margin: 7px;'><i class='fa fa-shopping-cart inner-right-vs'>VOIR DANS LE PANIER</i></a>|<button type='submit' class='btn btn-primary' style='margin: 7px;'><i class='fa fa-shopping-cart inner-right-vs'></i>AUGMENTER LA QUANTITE</a>")
              }
              else{
                submitSpan.html("<button type='submit' class='btn btn-primary'><i class='fa fa-shopping-cart inner-right-vs'></i>PAYER MAINTENANT</button>")
              }

              var navBarCount = $(".navbar-cart-count")
              var navBarCartSommeTotal = $(".cart-somme-total")
              navBarCount.text(data.cartItemsCount)
              console.log("Item du panier est : " ,navBarCount.text())
              navBarCartSommeTotal.text(data.cartSommeTotal)
              // var currentPath = window.location.href
              // if(currentPath.indexOf("") != -1){
              //   refreshHome()
              // }
              // if(currentPath.indexOf("cart") != -1){
              //   refreshCartPostAdd()
              // }
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

      // function refreshCartPostAdd(){
      //   console.log("In current cart for add")
      //   var cartTableHomeSomme = $(".cart-table-home-somme")
      //   var cartTableHome = $(".cart-table-home")
      //   var cartBodyHome = cartTableHome.find(".cart-body-home")
      //   var productRows = cartBodyHome.find(".cart-product-home")
      //   var currentUrl = window.location.href

      //   var refreshCartUrl = "/cart/api/cart/"
      //   var refreshCartMethod = "GET"
      //   var data = {}
      //   $.ajax({
      //     url : refreshCartUrl,
      //     method: refreshCartMethod,
      //     data: data,
      //     success : function(data){
      //       var hiddenCartRemoveForm = $(".cart-item-remove-form")
      //       if(data.products.length > 0){

      //       productRows.html(" ")
      //       i = 1
      //       $.each(data.products, function(index, value){
      //         var newCartItemRemove = hiddenCartRemoveForm.clone()
      //         newCartItemRemove.css("display", "block")
      //         newCartItemRemove.find(".cart-item-product-id").val(value.id)
      //         cartBodyHome.prepend("<tr><td class='romove-item'>" + newCartItemRemove.html() + " <td class='cart-image'><a class='entry-thumbnail' href='" + value.url +"'><img src=\"{% static 'images/products/p1.jpg' %}\" alt=''></a></td><td class='cart-product-name-info'><h4 class='cart-product-description'><a href='" + value.url + "'>" + value.name + "</a></h4><div class='row'><div class='col-sm-4'><div class='rating rateit-small'></div></div><div class='col-sm-8'><div class='reviews'>(06 Reviews)</div></div></div><div class='cart-product-info'><span class='product-color'>COLOR:<span>Blue</span></span></div></td><td class='cart-product-edit'><a href='" + value.url + "' class='product-edit'>Edit</a></td><td class='cart-product-quantity'><div class='quant-input'><div class='arrows'><div class='arrow plus gradient'><span class='ir'><i class='icon fa fa-sort-asc'></i></span></div><div class='arrow minus gradient'><span class='ir'><i class='icon fa fa-sort-desc'></i></span></div></div><input type='text' value='1'></div></td><td class='cart-product-sub-total'><span class='cart-sub-total-price'>$" + value.price + "</span></td><td class=cart-product-grand-total><span class=cart-grand-total-price>$" + value.price + "</span></td></tr> " )

      //       })

      //       cartTableHomeSomme.find(".cart-subtotal-home-somme").text(data.subtotal)
      //       cartTableHomeSomme.find(".cart-total-home-somme").text(data.total)
      //       console.log("Seperieur 0")
      //       totalText = cartBodyHome.find(".cart-total-home").text()
      //       console.log("Voici le total", data.total)

      //       }
      //       else{
      //         window.location.href = currentUrl
      //         console.log("inferieur à 0")
      //       }
      //       console.log("success")

      //       console.log(data)

      //     },

      //     error: function(errorData){
      //         $.alert({
      //           title: "oops !",
      //           content: "Une erreur s'est occasionée",
      //           theme: "modern",
      //         })
      //     }
      //   })

      // }

      // End Add update


      // Start Delete update

      var productFormDelete = $(".form-product-ajax-delete")
      productFormDelete.submit(function(event){
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
              var submitSpan = thisForm.find(".submit-span")
              if (data.deleted){
                submitSpan.html("<a href='/cart' class='btn btn-primary' style='margin: 7px;'><i class='fa fa-shopping-cart inner-right-vs'>VOIR DANS LE PANIER</i></a>|<button type='submit' class='btn btn-primary' style='margin: 7px;'><i class='fa fa-shopping-cart inner-right-vs'></i>ENLEVER DU PANIER</a>")
              }
              else{
                submitSpan.html("<button type='submit' class='btn btn-primary'><i class='fa fa-shopping-cart inner-right-vs'></i>PAYER MAINTENANT</button>")
              }

              var navBarCount = $(".navbar-cart-count")
              var navBarCartSommeTotal = $(".cart-somme-total")
              navBarCount.text(data.cartItemsCount)
              navBarCartSommeTotal.text(data.cartSommeTotal)
              var currentPath = window.location.href
              // if(currentPath.indexOf("") != -1){
              //   refreshHome()
              // }
              if(currentPath.indexOf("cart") != -1){
                refreshCartPostDelete()
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



      function refreshCartPostDelete(){
        console.log("In current cart for delete")
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
              console.log("L'url est :", value.url)
              cartBodyHome.prepend("<tr><td class='romove-item'>" + newCartItemRemove.html() + " <td class='cart-image'><a class='entry-thumbnail' href='" + value.url +"'><img src=\"{% static 'images/products/p1.jpg' %}\" alt=''></a></td><td class='cart-product-name-info'><h4 class='cart-product-description'><a href='" + value.url + "'>" + value.name + "</a></h4><div class='row'><div class='col-sm-4'><div class='rating rateit-small'></div></div><div class='col-sm-8'><div class='reviews'>(06 Reviews)</div></div></div><div class='cart-product-info'><span class='product-color'>COLOR:<span>Blue</span></span></div></td><td class='cart-product-edit'><a href='" + value.url + "' class='product-edit'>Edit</a></td><td class='cart-product-quantity'><div class='quant-input'><div class='arrows'><div class='arrow plus gradient'><span class='ir'><i class='icon fa fa-sort-asc'></i></span></div><div class='arrow minus gradient'><span class='ir'><i class='icon fa fa-sort-desc'></i></span></div></div><input type='text' value='1'></div></td><td class='cart-product-sub-total'><span class='cart-sub-total-price'>$" + value.price + "</span></td><td class=cart-product-grand-total><span class=cart-grand-total-price>$" + value.price + "</span></td></tr> " )

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






      // End Delete update










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

