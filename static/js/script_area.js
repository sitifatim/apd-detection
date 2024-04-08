const canvas = document.getElementById("polygonCanvas");
const ctx = canvas.getContext("2d");
let isDrawing = false;
let coordinates = [];
var idUuidHolder = document.getElementById("idUuidHolder");
var id_uuid = idUuidHolder.getAttribute("data-id_uuid");

// Function to draw a polygon on the canvas
function drawPolygon(coords) {
    ctx.beginPath();
    ctx.moveTo(coords[0][0], coords[0][1]);
    for (let i = 1; i < coords.length; i++) {
        ctx.lineTo(coords[i][0], coords[i][1]);
    }
    ctx.closePath();
    ctx.stroke();
}

// Get coordinates from Flask route and draw the polygons
function getCoordinatesAndDraw() {
    const toogleValue = document.querySelector('input[name="exampleRadios"]:checked').value;

    if (toogleValue === "yes") {
        fetch(`/get_coordinates/${id_uuid}`)
            .then(response => response.json())
            .then(data => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                coordinates = data;

                for (const key in coordinates) {
                    if (coordinates.hasOwnProperty(key)) {
                        drawPolygon(coordinates[key]);
                    }
                }
            })
            .catch(error => {
                console.error("Fetch error:", error);
            });
    } else {
        // Clear the canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        coordinates = [];
    }
}

// Attach event listeners to radio buttons
document.getElementById("noButton").addEventListener("change", getCoordinatesAndDraw);
document.getElementById("yesButton").addEventListener("change", getCoordinatesAndDraw);

// Initial drawing based on the default radio button state
getCoordinatesAndDraw();
