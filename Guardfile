# A sample Guardfile
# More info at https://github.com/guard/guard#readme

guard 'livereload' do
  watch(%r{vincent/apps/base/static/.+\.(css|js)$})
  watch(%r{vincent/apps/.+\.(jinja2)$})

end

guard 'compass' do
  watch(%r{vincent/apps/base/static/.+\.(sass|scss)$})
end

guard 'shell' do
  watch(%r{vincent/apps/base/static/vendor/bootstrap/less/.+\.less}) { `make -C vincent/apps/base/static/vendor/bootstrap/ bootstrap-css` }
  watch(%r{vincent/apps/base/static/images/icons/.+}) { `glue vincent/apps/base/static/images/icons/ --css=vincent/apps/base/static/css/sprite --img=vincent/apps/base/static/images/` }
end
