#!/bin/bash

echo "Running tests..."
echo "If you have npm installed, your browser will open with a test report on completion"
echo "Check README for troubleshooting"

if [ ! -d "allure-results/history" ]; then
    mkdir -p allure-results/history
fi

behave -f allure_behave.formatter:AllureFormatter -o allure-results features

if [ ! -d "allure-report/history" ]; then
    cp allure-report/history/* allure-results/history
fi

allure generate --clean --single-file allure-results

echo "Test report generated: allure-results/index.html"