document.addEventListener('DOMContentLoaded', function() {
    const seatMap = document.querySelector('.seat-map');
    if (seatMap) {
        seatMap.addEventListener('click', function(event) {
            const seat = event.target;
            if (seat.classList.contains('available')) {
                seat.classList.toggle('selected');
                updatePrice();
            }
        });
    }

    function updatePrice() {
        const selectedSeats = document.querySelectorAll('.seat.selected');
        const pricePerSeat = 10; 
        const totalPrice = selectedSeats.length * pricePerSeat;
        document.querySelector('.total-price').textContent = `Total: $${totalPrice}`;
    }

});