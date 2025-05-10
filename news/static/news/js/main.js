// Рандомные глитч-эффекты
document.addEventListener('DOMContentLoaded', () => {
    // Каждые 5 секунд — случайный "баг"
    setInterval(() => {
        document.body.classList.add('glitch-active');
        setTimeout(() => {
            document.body.classList.remove('glitch-active');
        }, 300);
    }, 5000);

    // Кнопки мигают как неон
    const buttons = document.querySelectorAll('.btn-cyber');
    buttons.forEach(btn => {
        btn.addEventListener('mouseover', () => {
            btn.style.animation = 'neon-flicker 0.5s infinite alternate';
        });
        btn.addEventListener('mouseout', () => {
            btn.style.animation = 'none';
        });
    });
});
