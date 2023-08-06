document.addEventListener('DOMContentLoaded', function() {
    const restaurantSelect = document.getElementById('restaurantSelect');
    const dishesContainer = document.getElementById('dishesContainer');

    // Function to remove all elements inside the dishesContainer
  function removeAllChildNodes(parent) {
      while (parent.firstChild) {
          parent.removeChild(parent.firstChild);
      }
  }

    // Function to fetch dishes based on the selected restaurant
    function fetchDishes(selectedRestaurantId) {
        fetch("getdishes/" + selectedRestaurantId + "?restaurant=" + selectedRestaurantId)
            .then(response => response.json())
            .then(data => {
                // Clear previous checkboxes
                dishesContainer.innerHTML = '';

                // Generate checkboxes for each dish
                data.dishes.forEach(dish => {
                  const checkboxDiv = document.createElement('div');
                  checkboxDiv.classList.add('form-check');

                  const checkboxInput = document.createElement('input');
                  checkboxInput.type = 'checkbox';
                  checkboxInput.classList.add('form-check-input');
                  checkboxInput.id = `dishCheckbox${dish.dish_id}`;
                  checkboxInput.name = 'selected_dishes';
                  checkboxInput.value = dish.dish_id;

                  checkboxInput.setAttribute('data-dish-name', dish.dish_name);
                  checkboxInput.setAttribute('data-dish-price', dish.dish_price);
                  checkboxInput.setAttribute('data-dish-id', dish.dish_id);

                  const label = document.createElement('label');
                  label.classList.add('form-check-label');
                  label.setAttribute('for', `dishCheckbox${dish.dish_id}`);
                  label.textContent = `${dish.dish_name} - RD$${dish.dish_price}`;

                  checkboxDiv.appendChild(checkboxInput);
                  checkboxDiv.appendChild(label);

                  dishesContainer.appendChild(checkboxDiv);

                });
                getSelectedCheckbox();
            })
            .catch(error => {
                // Handle error
                console.error('Error:', error);
            });
    }

    // Initial fetch for the selected restaurant
    fetchDishes(restaurantSelect.value);
    

    // Listen for changes in the select element
    restaurantSelect.addEventListener('change', function(event) {
        // Get the selected restaurant ID from the select option
        const selectedRestaurantId = event.target.value;

        // Clear previous checkboxes
        removeAllChildNodes(dishesContainer)

        // Fetch dishes based on the selected restaurant
        fetchDishes(selectedRestaurantId);
    });

  function getSelectedCheckbox(){
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const selectedDishesContainer = document.getElementById('selectedDishesContainer');
    const selectedDishes = []; // Array to store selected dishes

    // Loop through each checkbox and attach the event listener
      checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function(event) {
          if (event.target.checked) {
                  // Checkbox is checked, add it to the selected dishes container
                  const selectedDishName = event.target.getAttribute('data-dish-name');
                  const selectedDishPrice = event.target.getAttribute('data-dish-price');
                  const selectedDishId = event.target.getAttribute('data-dish-id');
                  const selectedDishRow = document.createElement('div');
                  selectedDishRow.classList.add('row');

                  const dishNameCol = document.createElement('div');
                  dishNameCol.classList.add('col');
                  dishNameCol.textContent = selectedDishName;

                  const dishPriceCol = document.createElement('div');
                  dishPriceCol.classList.add('fw-bold', 'col');
                  dishPriceCol.textContent = `RD$${selectedDishPrice}`;

                  selectedDishRow.appendChild(dishNameCol);
                  selectedDishRow.appendChild(dishPriceCol);

                  selectedDishesContainer.prepend(selectedDishRow);

                  // Store the selected dish data in the array
                  selectedDishes.push({
                      id: selectedDishId,
                      name: selectedDishName,
                      price: selectedDishPrice
                  });

                  var totalPrice = parseFloat(document.getElementById("budgetPriceContainer").getAttribute("data-price"));
                  totalPrice += parseFloat(selectedDishPrice);

                  
                  var youpayBudget = parseFloat(document.getElementById("youpayContainer").getAttribute("data-pay"));
                  youpayBudget = parseFloat(totalPrice - 75);

            } else {
              // Checkbox is unchecked, remove it from the selected dishes container
                const selectedDishRow = document.getElementById("dishCheckbox"+selectedDishId);
                selectedDishRow.remove();
            }

            const budgetPriceContainer = document.getElementById('budgetPriceContainer');
            budgetPriceContainer.textContent = `RD$${totalPrice.toFixed(2)}`;
            budgetPriceContainer.setAttribute("data-price",totalPrice);

            const youpayContainer = document.getElementById('youpayContainer');
            youpayContainer.textContent = `RD$${youpayBudget.toFixed(2)}`;
            youpayContainer.setAttribute("data-pay",youpayBudget); 

            // Update the hidden input value with the updated JSON string
            const hiddenInput = document.getElementById('selectedDishesInput');
            hiddenInput.value = JSON.stringify(selectedDishes);
        });
    });
}

    

});