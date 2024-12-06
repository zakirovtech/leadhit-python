echo 'Переданы все поля целевой формы'
curl -X POST http://localhost:8000/get_form/ -H "Content-Type: application/x-www-form-urlencoded" -d "survey_date=2024-12-01&feedback_text=Very+satisfied+with+the+product.&respondent_email=survey.user@example.net&some_feild=2"

echo ""

echo 'Передан неправильный тип в одном поле формы'
curl -X POST http://localhost:8000/get_form/ -H "Content-Type: application/x-www-form-urlencoded" -d "survey_date=2024-12-01&feedback_text=Very+satisfied+with+the+product.&respondent_email=survey.user_example.net&some_feild=2"

echo ""