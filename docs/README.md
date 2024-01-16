# Candy_Problem_in_Python

[![License: AGPL](https://img.shields.io/badge/License-AGPL-blue.svg)](https://github.com/gotreasa/candy_problem_in_python/blob/main/LICENSE)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_candy_problem_in_python&metric=alert_status)](https://sonarcloud.io/dashboard?id=gotreasa_candy_problem_in_python)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_candy_problem_in_python&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=gotreasa_candy_problem_in_python)
[![Build Status](https://github.com/gotreasa/candy_problem_in_python/actions/workflows/cicd.yml/badge.svg)](https://github.com/gotreasa/candy_problem_in_python/actions/workflows/cicd.yml)
[![Can I Deploy main to test](https://gotreasa.pactflow.io/pacticipants/candy_problem_in_python_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)](https://gotreasa.pactflow.io/hal-browser/browser.html#https://gotreasa.pactflow.io/pacticipants/candy_problem_in_python_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)

Welcome to the Python Template created via a cookiecutter recipe. The project template is designed for a development via a `Double Loop approach` (BDD-TDD) using pytest and several other pytest libs.

## Description

"It's the end of trick-or-treating and we have a list/array representing how much candy each child in our group has made out with. We don't want the kids to start arguing, and using our parental intuition we know trouble is brewing as many of the children in the group have received different amounts of candy from each home.

So we want each child to have the same amount of candies, only we can't exactly take any candy away from the kids, that would be even worse. Instead we decide to give each child extra candy until they all have the same amount.

### Task

Your job is to find out how much candy each child has, and give them each additional candy until they too have as much as the child(ren) with the most candy. You also want to keep a total of how much candy you've handed out because reasons."

Your job is to give all the kids the same amount of candies as the kid with the most candies and then return the total number candies that have been given out. If there are no kids, or only one, return -1.

In the first case (look below) the most candies are given to second kid (i.e second place in list/array), 8. Because of that we will give the first kid 3 so he can have 8 and the third kid 2 and the fourth kid 4, so all kids will have 8 candies. So we end up handing out 3 + 2 + 4 = 9.

```
(5, 8, 6, 4) =>  9
(1, 2, 4, 6) => 11
(1, 6)       =>  5
( )          => -1
(6)          => -1 (because only one kid)
```
